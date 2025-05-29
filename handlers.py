from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards import (
    create_main_menu_keyboard,
    create_routes_keyboard,
    create_nav_keyboard, create_contacts_keyboard
)
from models import ROUTES, PROJECT_INFO
import os

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎧 Добро пожаловать в аудиогид по Санкт-Петербургу!",
        reply_markup=create_main_menu_keyboard()
    )


@router.callback_query(F.data == "main_menu")
async def handle_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=create_main_menu_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == "routes_menu")
async def handle_routes_menu(callback: types.CallbackQuery):
    try:
        await callback.message.edit_text(
            "Выберите маршрут:",
            reply_markup=create_routes_keyboard()
        )
    except Exception:
        await callback.message.delete()
        await callback.message.answer(
            "Выберите маршрут:",
            reply_markup=create_routes_keyboard()
        )
    finally:
        await callback.answer()


@router.callback_query(F.data == "contacts")
async def handle_contacts(callback: types.CallbackQuery):
    try:
        # Формируем текст с кликабельными ссылками
        contacts_text = (
            "📞 <b>Контакты разработчиков:</b>\n\n"
            "• <a href='https://t.me/ArinaRromanova'>Арина</a>\n"
            "• <a href='https://t.me/FilatovaElina1'>Элина</a>\n"
            "• <a href='https://t.me/artemartemmmmmm'>Артём</a>\n"
            "• <a href='https://t.me/helldreamm'>Иван</a>\n"
            "• <a href='https://t.me/libik891'>Ильдар</a>\n\n"
            "Cсылка на сайт: " + PROJECT_INFO["website"]
        )

        # Отправляем сообщение с клавиатурой
        await callback.message.edit_text(
            contacts_text,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=create_contacts_keyboard()
        )
    except Exception:
        # Если не получилось отредактировать (например, было аудио)
        await callback.message.delete()
        await callback.message.answer(
            contacts_text,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=create_contacts_keyboard()
        )
    finally:
        await callback.answer()

@router.callback_query(F.data == "about")
async def handle_about(callback: types.CallbackQuery):
    await callback.answer(
        PROJECT_INFO['about'],
        show_alert=True
    )


@router.callback_query(F.data.startswith("route_"))
async def handle_route_selection(callback: types.CallbackQuery):
    route_id = callback.data.split("_")[1]
    route_data = ROUTES[route_id]

    # Отправляем ссылку
    await callback.message.answer(
        f"🔗 {route_data['name']}\nСсылка на маршрут: {route_data['link']}"
    )

    # Отправляем первое аудио
    audio_path = route_data["audios"][0]
    with open(audio_path, "rb") as audio_file:
        await callback.message.answer_audio(
            audio=types.BufferedInputFile(
                audio_file.read(),
                filename=os.path.basename(audio_path)
            ),
            caption=f"Точка 1/{len(route_data['audios'])}",
            reply_markup=create_nav_keyboard(route_id, 0)
        )

    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith("nav_"))
async def handle_navigation(callback: types.CallbackQuery):
    try:
        _, route_id, step = callback.data.split("_")
        step = int(step)
        route_data = ROUTES[route_id]

        print(f"Навигация: маршрут {route_id}, шаг {step}")  # Отладочный вывод
        print(f"Всего шагов: {len(route_data['audios'])}")  # Отладочный вывод

        audio_path = route_data["audios"][step]

        with open(audio_path, "rb") as audio_file:
            await callback.message.answer_audio(
                audio=types.BufferedInputFile(
                    audio_file.read(),
                    filename=os.path.basename(audio_path)
                ),
                caption=f"{route_data['name']} (точка {step + 1}/{len(route_data['audios'])})",
                reply_markup=create_nav_keyboard(route_id, step)
            )
        await callback.message.delete()
    except Exception as e:
        print(f"Ошибка навигации: {str(e)}")  # Отладочный вывод
        await callback.answer(f"⚠️ Ошибка: {str(e)}", show_alert=True)
    finally:
        await callback.answer()