from data.messages import *
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

'''
    Поиск заявки:
        по id
        по услуге
        по дате
        по статусу
        по номеру телефона
        
    Изменение заявки
        изм. статуса
        изм. комментария
        изм. цены

'''


def adm_menu_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=adm_search, callback_data='adm_search'),
        InlineKeyboardButton(text=adm_change, callback_data='adm_change'),
        InlineKeyboardButton(text=adm_switch_user_menu, callback_data='adm_switch_user_menu'),
        width=1
    )


def adm_search_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=search_id, callback_data='search_id'),
        InlineKeyboardButton(text=search_sr, callback_data='search_sr'),
        InlineKeyboardButton(text=search_dt, callback_data='search_dt'),
        InlineKeyboardButton(text=search_st, callback_data='search_st'),
        InlineKeyboardButton(text=search_pn, callback_data='search_pn'),
        width=1
    )


def adm_change_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=change_stus, callback_data='change_stus'),
        InlineKeyboardButton(text=change_prce, callback_data='change_prce'),
        InlineKeyboardButton(text=change_comm, callback_data='change_comm'),
        width=1
    )


def adm_check_service_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=serv_1, callback_data='service_1'),
        InlineKeyboardButton(text=serv_2, callback_data='service_2'),
        InlineKeyboardButton(text=serv_3, callback_data='service_3'),
        InlineKeyboardButton(text=serv_4, callback_data='service_4'),
        InlineKeyboardButton(text=serv_5, callback_data='service_5'),
        InlineKeyboardButton(text=serv_6, callback_data='service_6'),
        InlineKeyboardButton(text=serv_7, callback_data='service_7'),
        InlineKeyboardButton(text=serv_8, callback_data='service_8'),
        InlineKeyboardButton(text=serv_9, callback_data='service_9'),
        InlineKeyboardButton(text=serv_10, callback_data='service_10'),
        width=1
    )


def adm_check_app_status_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=appstatus_1, callback_data='appstatus_1'),
        InlineKeyboardButton(text=appstatus_2, callback_data='appstatus_2'),
        InlineKeyboardButton(text=appstatus_3, callback_data='appstatus_3'),
        InlineKeyboardButton(text=appstatus_4, callback_data='appstatus_4'),
        InlineKeyboardButton(text=appstatus_5, callback_data='appstatus_5'),
        InlineKeyboardButton(text=appstatus_6, callback_data='appstatus_6'),
        width=1
    )


def adm_change_app_status_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=appstatus_1, callback_data='ch#appstatus_1'),
        InlineKeyboardButton(text=appstatus_2, callback_data='ch#appstatus_2'),
        InlineKeyboardButton(text=appstatus_3, callback_data='ch#appstatus_3'),
        InlineKeyboardButton(text=appstatus_4, callback_data='ch#appstatus_4'),
        InlineKeyboardButton(text=appstatus_5, callback_data='ch#appstatus_5'),
        InlineKeyboardButton(text=appstatus_6, callback_data='ch#appstatus_6'),
        width=1
    )
