from api import PetFriends
from settings import valid_email, valid_password
import os

pf=PetFriends()


def test_get_api_key_for_valid_user(email=valid_email , password= valid_password ):
    status, result= pf.get_api_key(email , password  )
    assert status == 200
    assert "key" in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password )
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0


def test_add_new_pet_with_valid_data(name='Sam', animal_type='dog',
                                     age='4', pet_photo='images/dog.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Cat", "Cat", "3", "images/cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Bubble', animal_type='fish', age=1):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


# 10 дополнительных тестов:

def test_get_api_key_for_no_valid_email(email = 'dompitomcha@mail.ru', password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_api_key_for_no_valid_password(email = valid_email , password = '8749DoM'):
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_api_key_for_no_empty_password(email = valid_email , password = None ):
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_add_new_pet_with_no_valid_key(name="Dan", animal_type="parrow", age=3, pet_photo='images/bird.jpg'):
    auth_key = {"key": '8a417540fe39eae66f0bcdbafd453e1fadfc2bf1b50cbc0d634b1fa1'}
    status, result = pf.add_new_pet(auth_key,name,animal_type, age, pet_photo)
    assert status == 403

def test_add_new_pet_with_no_valid_age(name='Mila', animal_type='cat',
                                     age='%gbhsrt', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400


def test_add_new_pet_with_no_walid_numbers_of_characters_name(name='Simonononononononononononononononononononononononononononononononononononononononononnonononononononononono', animal_type='cat',
                                     age='2', pet_photo='images/cat1.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_delete_pet_with_valid_data_no_valid_key(pet_id=''):
    auth_key = {"key": '8a417540fe39eae66f0bcdbafd453e1fadfc2bf1b50cbc0d634b1fa1'}
    status, _ = pf.delete_pet(auth_key,pet_id)
    assert status == 404


def test_not_successful_update_self_pet_info(name='Bubble', animal_type='fish', age='vcvcxxx'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")



def test_not_successful_update_self_pet_info(name='Bubble', animal_type='fish', age=1):

    auth_key = {"key": '8a417540fe39eae66f0bgjggj86nfggmht6u68nd '}
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")
