from aiogram import Router, F
from keyboards.admin_kb import *
from services.app_form_service import *
from aiogram.fsm.context import FSMContext
from roloc_create import roloc_bot, ADMIN_ID
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

change_router = Router()


class AdminDataForChange(StatesGroup):
    admin_change_id_prce = State()
    admin_change_id_comm = State()
    admin_change_id_stus = State()

    admin_change_price = State()
    admin_change_comment = State()
    admin_change_status = State()


@change_router.callback_query(F.data.startswith('adm_change'))
async def admin_change_menu_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        await state.clear()
        await callback.answer()
        await callback.message.edit_text(msg_change_param, reply_markup=adm_change_kb().as_markup())


@change_router.callback_query(F.data.startswith('change'))
async def admin_change_options_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        call_data = callback.data.split('_')[1]
        await callback.answer()
        if call_data == 'stus':
            await state.set_state(AdminDataForChange.admin_change_id_stus)
            await callback.message.edit_text(msg_search_number)

        elif call_data == 'prce':
            await state.set_state(AdminDataForChange.admin_change_id_prce)
            await callback.message.edit_text(msg_search_number)

        elif call_data == 'comm':
            await state.set_state(AdminDataForChange.admin_change_id_comm)
            await callback.message.edit_text(msg_search_number)


''' CHANGE STATUS '''


@change_router.message(AdminDataForChange.admin_change_id_stus)
async def change_status1_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForChange:admin_change_id_stus':
        await state.update_data(app_status_id=msg.text)
        await state.set_state(AdminDataForChange.admin_change_status)
        await roloc_bot.send_message(msg.from_user.id, msg_search_status,
                                     reply_markup=adm_change_app_status_kb().as_markup())


@change_router.message(AdminDataForChange.admin_change_status)
@change_router.callback_query(F.data.startswith('ch'))
async def change_status2_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        state_data = await state.get_data()
        await state.clear()
        await callback.answer()

        app_id = state_data['app_status_id']
        status = app_status_dict[callback.data.split('#')[1]]

        result = update_status(status, app_id)

        if result is None:
            return callback.message.edit_text(msg_noexs_number, reply_markup=adm_menu_kb().as_markup())

        if not result:
            await callback.message.edit_text(msg_change_failed_stats, reply_markup=adm_menu_kb().as_markup())
        else:
            await callback.message.edit_text(msg_change_success_stats, reply_markup=adm_menu_kb().as_markup())


''' CHANGE PRICE '''


@change_router.message(AdminDataForChange.admin_change_id_prce)
async def change_price1_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForChange:admin_change_id_prce':
        await state.update_data(app_price_id=msg.text)
        await state.set_state(AdminDataForChange.admin_change_price)
        await roloc_bot.send_message(msg.from_user.id, msg_change_price)


@change_router.message(AdminDataForChange.admin_change_price)
async def change_price2_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForChange:admin_change_price':
        await state.update_data(price=msg.text)
        state_data = await state.get_data()
        await state.clear()

        result = update_price(state_data['price'], state_data['app_price_id'])
        if result is None:
            await roloc_bot.send_message(ADMIN_ID, msg_noexs_number, reply_markup=adm_menu_kb().as_markup())

        elif not result:
            await roloc_bot.send_message(ADMIN_ID, msg_change_failed_price, reply_markup=adm_menu_kb().as_markup())

        else:
            await roloc_bot.send_message(ADMIN_ID, msg_change_success_price, reply_markup=adm_menu_kb().as_markup())


''' CHANGE COMMENT '''


@change_router.message(AdminDataForChange.admin_change_id_comm)
async def change_comm1_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForChange:admin_change_id_comm':
        await state.update_data(app_comment_id=msg.text)
        await state.set_state(AdminDataForChange.admin_change_comment)
        await roloc_bot.send_message(msg.from_user.id, msg_change_commt)


@change_router.message(AdminDataForChange.admin_change_comment)
async def change_comm2_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForChange:admin_change_comment':
        await state.update_data(comment=msg.text)
        state_data = await state.get_data()
        await state.clear()

        result = update_comment(state_data['comment'], state_data['app_comment_id'])
        if result is None:
            await roloc_bot.send_message(ADMIN_ID, msg_noexs_number, reply_markup=adm_menu_kb().as_markup())

        if not result:
            await roloc_bot.send_message(ADMIN_ID, msg_change_failed_commt, reply_markup=adm_menu_kb().as_markup())
        else:
            await roloc_bot.send_message(ADMIN_ID, msg_change_success_commt, reply_markup=adm_menu_kb().as_markup())
