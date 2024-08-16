from aiogram.filters import Command

from data.messages import *
from aiogram import Router, F

from keyboards.user_kb import user_menu_kb
from aiogram.fsm.context import FSMContext
from roloc_create import roloc_bot, ADMIN_ID
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State

help_router = Router()


class HelpState(StatesGroup):
    name = State()
    helptext = State()
    contacts = State()


@help_router.message(Command('help'))
async def user_help_command(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(HelpState.name)
    await roloc_bot.send_message(msg.from_user.id, msg_uname)


@help_router.callback_query(F.data.startswith('menu_3'))
async def user_help_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(HelpState.name)
    await callback.message.edit_text(msg_uname)


@help_router.message(HelpState.name)
async def user_help_name(msg: Message, state: FSMContext):
    if not msg.text:
        await roloc_bot.send_message(msg.from_user.id, msg_media)
        await state.set_state(HelpState.name)
        await roloc_bot.send_message(msg.from_user.id, msg_uname)
    else:
        await state.update_data(name=msg.text)
        await state.set_state(HelpState.helptext)
        await roloc_bot.send_message(msg.from_user.id, msg_uprbl)


@help_router.message(HelpState.helptext)
async def user_help_text(msg: Message, state: FSMContext):
    if not msg.text:
        await roloc_bot.send_message(msg.from_user.id, msg_media)
        await state.set_state(HelpState.helptext)
        await roloc_bot.send_message(msg.from_user.id, msg_uprbl)
    else:
        await state.update_data(helptext=msg.text)
        await state.set_state(HelpState.contacts)
        await roloc_bot.send_message(msg.from_user.id, msg_contc)


@help_router.message(HelpState.contacts)
async def user_help_contact(msg: Message, state: FSMContext):
    if not msg.text:
        await roloc_bot.send_message(msg.from_user.id, msg_media)
        await state.set_state(HelpState.contacts)
        await roloc_bot.send_message(msg.from_user.id, msg_contc)
    else:
        user_id = msg.from_user.id
        user_tg_data = [
            user_id,
            msg.from_user.username,
        ]

        await state.update_data(contacts=msg.text)
        user_help_data = await state.get_data()

        await state.clear()

        text = text_perform(user_tg_data, user_help_data)
        await roloc_bot.send_message(ADMIN_ID, text)
        await roloc_bot.send_message(user_id, msg_procd, reply_markup=user_menu_kb().as_markup())


def text_perform(tg_data: list, help_data: dict):
    user_id = tg_data[0]
    username = tg_data[1]
    name = help_data['name']
    help_text = help_data['helptext']
    contacts = help_data['contacts']

    if username is None:
        username = "-"

    return (f"🆘 <strong>ПОМОЩЬ</strong>\n\n"
            f"👨‍💻 Пользователь:\n"
            f"• ID: <code>{user_id}</code>\n"
            f"• Username: <code>@{username}</code>\n"
            f"• Имя: {name}\n"
            f"• Контакты: <code>{contacts}</code>\n\n"
            f"✏️<strong>:</strong> {help_text}"
            )
