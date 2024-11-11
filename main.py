import instaloader
import json

insta = instaloader.Instaloader()

user_name = input('User name: ')
password = input('Password: ')

try:
    insta.login(user_name, password)

except instaloader.TwoFactorAuthRequiredException:
    print('Two-factor authentication enable. Enter the 2FA code.')
    two_factor_code = input('Two-factor code: ')
    insta.two_factor_login(two_factor_code)

profile_user  = instaloader.Profile.from_username(insta.context, user_name)
followers_profiles = list(profile_user.get_followers())

list_followers = ['@'+profile.username for profile in followers_profiles]

with open ('list_followers.json', 'w') as file:
    json.dump(list_followers, file)

print('List of followers has been saved in "list_followers.json"')

