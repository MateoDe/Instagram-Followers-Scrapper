from igramscraper.instagram import Instagram
from time import sleep
import csv

instagram = Instagram()

def seguidores(user):
    try:
        username = user
        followers = []
        account = instagram.get_account(username)
        sleep(1)
        followers = instagram.get_followers(account.identifier, 6000, 100, delayed=True) # Get 150 followers of 'kevin', 100 a time with random delay between requests

        for follower in followers['accounts']:
            print(follower.username)
            with open(f'{username}_seguidores.csv', 'a+') as f:
                f.write(f'{follower.username}\n')
    except:
        print(f'Usuario {user} no existe')

def seguidos(user):
    try:
        username = user
        following = []
        account = instagram.get_account(username)
        sleep(1)
        following = instagram.get_following(account.identifier, 6000, 100, delayed=True) 
        for following_user in following['accounts']:
            with open(f'{username}_seguidos.csv', 'a+') as f:
                f.write(f'{following_user.username}\n')
    except:
        pass
def run():
    username = input('User to scrape? : ')
    seguidores(username)
    seguidos(username)

if __name__ == '__main__':
    print('LOGIN: \n-----\n')
    user = input('Username: ')
    passwrd = input('Password: ')
    instagram.with_credentials(user, passwrd)
    try:
        instagram.login()
        run()
    except:
        print('LOGIN ERROR, AUTHORIZE THE DEVICE')
