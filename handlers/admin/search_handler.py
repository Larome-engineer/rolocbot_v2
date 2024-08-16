from aiogram import Router, F
from keyboards.admin_kb import *
from services.app_form_service import *
from aiogram.fsm.context import FSMContext
from roloc_create import roloc_bot, ADMIN_ID
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

search_router = Router()


class AdminDataForSearch(StatesGroup):
    admin_search_id = State()
    admin_search_date = State()
    admin_search_phone = State()


@search_router.callback_query(F.data.startswith('adm_search'))
async def admin_search_menu_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        await state.clear()
        await callback.answer()
        await callback.message.edit_text(msg_search_option, reply_markup=adm_search_kb().as_markup())


@search_router.callback_query(F.data.startswith('search'))
async def admin_search_options_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        call_data = callback.data.split('_')[1]
        await callback.answer()
        if call_data == 'id':
            await state.set_state(AdminDataForSearch.admin_search_id)
            await callback.message.edit_text(msg_search_number)

        elif call_data == 'sr':
            await callback.message.edit_text(msg_search_srvice, reply_markup=adm_check_service_kb().as_markup())

        elif call_data == 'dt':
            await state.set_state(AdminDataForSearch.admin_search_date)
            await callback.message.edit_text(msg_search_chdate)

        elif call_data == 'st':
            await callback.message.edit_text(msg_search_status, reply_markup=adm_check_app_status_kb().as_markup())

        elif call_data == 'pn':
            await state.set_state(AdminDataForSearch.admin_search_phone)
            await callback.message.edit_text(msg_search_uphone)


@search_router.callback_query(F.data.startswith('appstatus'))
async def by_status_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        await state.clear()
        await callback.answer()

        status = app_status_dict[callback.data]
        result = all_apps_by_status(status)

        if result is None:
            await callback.message.edit_text(msg_noexs_status, reply_markup=adm_menu_kb().as_markup())

        elif not result:
            await callback.message.edit_text(msg_error, reply_markup=adm_menu_kb().as_markup())

        else:
            await get_result(callback, result)


@search_router.callback_query(F.data.startswith('service'))
async def by_service_handler(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == ADMIN_ID:
        await state.clear()
        await callback.answer()

        data = callback.data
        service = c_match[f"{data[0:4:1]}_{data[-1]}"]
        result = all_apps_by_service(service)

        if result is None:
            await callback.message.edit_text(msg_noexs_srvice, reply_markup=adm_menu_kb().as_markup())

        elif not result:
            await callback.message.edit_text(msg_error, reply_markup=adm_menu_kb().as_markup())

        else:
            await get_result(callback, result)


@search_router.message(AdminDataForSearch.admin_search_id)
async def by_id_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForSearch:admin_search_id':
        await state.clear()
        result = app_info_by_number(msg.text)

        if result is None:
            await roloc_bot.send_message(ADMIN_ID, msg_noexs_number, reply_markup=adm_menu_kb().as_markup())

        elif not result:
            await roloc_bot.send_message(ADMIN_ID, msg_error, reply_markup=adm_menu_kb().as_markup())

        else:
            await get_result(msg, result)


@search_router.message(AdminDataForSearch.admin_search_date)
async def admin_check_by_app_date_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForSearch:admin_search_date':
        await state.clear()
        result = all_apps_by_date(msg.text)

        if result is None:
            await roloc_bot.send_message(ADMIN_ID, msg_noexs_sldate, reply_markup=adm_menu_kb().as_markup())

        elif not result:
            await roloc_bot.send_message(ADMIN_ID, msg_error, reply_markup=adm_menu_kb().as_markup())

        else:
            await get_result(msg, result)


@search_router.message(AdminDataForSearch.admin_search_phone)
async def admin_check_by_app_usr_phone_handler(msg: Message, state: FSMContext):
    ste = await state.get_state()
    if msg.from_user.id == ADMIN_ID and ste == 'AdminDataForSearch:admin_search_phone':
        await state.clear()
        result = all_apps_by_usr_phone(msg.text)

        if result is None:
            await roloc_bot.send_message(ADMIN_ID, msg_noexs_uphone, reply_markup=adm_menu_kb().as_markup())

        elif not result:
            await roloc_bot.send_message(ADMIN_ID, msg_error, reply_markup=adm_menu_kb().as_markup())

        else:
            await get_result(msg, result)


async def get_result(message: Message | CallbackQuery, result: str):
    if type(message) is CallbackQuery:
        count = len(result) // 4090

        if len(result) > 4090:
            for it in range(0, len(result), 4090):
                if it // 4090 == count:
                    await roloc_bot.send_message(message.from_user.id, result[it:it + 4090],
                                                 reply_markup=adm_menu_kb().as_markup())
                else:
                    await roloc_bot.send_message(message.from_user.id, result[it:it + 4090])
        else:
            await message.message.edit_text(result, reply_markup=adm_menu_kb().as_markup())

    else:
        count = len(result) // 4090

        if len(result) > 4090:
            for it in range(0, len(result), 4090):
                if it // 4090 == count:
                    await roloc_bot.send_message(message.from_user.id, result[it:it + 4090],
                                                 reply_markup=adm_menu_kb().as_markup())
                else:
                    await roloc_bot.send_message(message.from_user.id, result[it:it + 4090])
        else:
            await roloc_bot.send_message(message.from_user.id, result, reply_markup=adm_menu_kb().as_markup())
