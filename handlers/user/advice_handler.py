from aiogram import Router, F
from data.messages import msg_pdf
from data.config import ADV_FILE
from keyboards.user_kb import user_pdf_kb
from roloc_create import roloc_bot
from aiogram.types import CallbackQuery, FSInputFile

advice_router = Router()

@advice_router.callback_query(F.data.startswith('usermenu6'))
async def get_advice(callback: CallbackQuery):
    await callback.answer()
    await roloc_bot.send_document(callback.from_user.id,
                                  document=FSInputFile(ADV_FILE),
                                  caption=msg_pdf,
                                  reply_markup=user_pdf_kb().as_markup())

