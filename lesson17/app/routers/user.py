from fastapi import APIRouter
router = APIRouter(prefix='/user', tags=['user'])

@router.get('/all_users')
async def all_users():
    pass

@router.get('/user_id')
async def user_by_id():
    pass

@router.post('/create')
async def creaty_user():
    pass

@router.put('/update_user')
async def update_user():
    pass

@router.delete('/delete')
async def delete_user():
    pass