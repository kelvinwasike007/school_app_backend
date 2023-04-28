from fastapi import APIRouter
from ..models import accounts
router = APIRouter(
    prefix='/account',
    tags = ['User Accounts Management']
)

@router.post('/login')
def login_user():
    """Log in a User"""
    return accounts.login()

@router.post('/register')
def add_user():
    """Create a user account"""
    return accounts.createaccount()

@router.put('/update')
def edit_user():
    """Updates a user info"""
    return accounts.updateaccount()

@router.delete('/delete')
def delete_user():
    """Deletes a user account"""
    return accounts.deleteaccount()

@router.get('/')
def users():
    """Get list of all accounts"""
    return accounts.accountlist()
