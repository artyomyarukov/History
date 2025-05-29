from aiogram.utils.keyboard import InlineKeyboardBuilder
from models import ROUTES

def create_main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🗺️ Маршруты", callback_data="routes_menu")
    builder.button(text="📞 Контакты", callback_data="contacts")
    builder.button(text="ℹ️ О проекте", callback_data="about")
    builder.adjust(2, 2)
    return builder.as_markup()

def create_routes_keyboard():
    builder = InlineKeyboardBuilder()
    for route_id, route_data in ROUTES.items():
        builder.button(
            text=route_data["name"],
            callback_data=f"route_{route_id}"
        )
    builder.button(text="🔙 Назад", callback_data="main_menu")
    builder.adjust(1)
    return builder.as_markup()

def create_nav_keyboard(route_id: str, step: int):
    builder = InlineKeyboardBuilder()
    if step > 0:
        builder.button(text="⬅️ Назад", callback_data=f"nav_{route_id}_{step-1}")
    builder.button(text="🗺️ К маршрутам", callback_data="routes_menu")
    if step < len(ROUTES[route_id]["audios"]) - 1:
        builder.button(text="Далее ➡️", callback_data=f"nav_{route_id}_{step+1}")
    builder.adjust(2, 1)
    return builder.as_markup()

def create_contacts_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Назад", callback_data="main_menu")
    return builder.as_markup()