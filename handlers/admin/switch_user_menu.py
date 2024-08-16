from aiogram import Router, F
from keyboards.admin_kb import *
from keyboards.user_kb import user_menu_kb
from aiogram.fsm.context import FSMContext
from roloc_create import ADMIN_ID
from aiogram.types import CallbackQuery

switch_router = Router()


@switch_router.callback_query(F.data.startswith('adm_switch_user_menu'))
async def switch_user_menu(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        await state.clear()
        await callback.answer()
        await callback.message.edit_text(msg_umenu, reply_markup=user_menu_kb().as_markup())
