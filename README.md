# BipolarFactory-task

## 1. Post Request to register a new User
![WhatsApp Image 2024-03-01 at 07 26 57_682e9303](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/a16e48df-478b-42a6-bb0f-7bc28114b228)

## 2. Post Request to login a new User
![WhatsApp Image 2024-03-01 at 07 27 31_62e1c7c8](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/5c7509e3-947d-492d-a251-2c918820143f)

## 3. Post Request to create Flight by Admin
![WhatsApp Image 2024-03-01 at 07 48 40_870e7c75](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/f12e22f3-217a-4c64-8349-4f9e07d348a8)

## 4. Get Request to view all Flight Details
![WhatsApp Image 2024-03-01 at 07 28 39_ad9f772d](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/aee25e84-4663-4f5b-924e-cf45c4124846)

## 5. Get Request to view a particular Flight Details
![WhatsApp Image 2024-03-01 at 07 28 59_05092c19](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/5e22a8c8-33cb-43fc-be80-68d2fe9eec54)

## 6. Get Request to view all the Bookings
### User's Bookings
![WhatsApp Image 2024-03-01 at 07 45 52_4552528d](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/2bdd169c-0a49-45f4-86e7-ecff0f9199d5)

### All Bookings for Admin
![WhatsApp Image 2024-03-01 at 07 47 35_c618c126](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/7f289baf-698f-4ff6-9027-c77c40727718)


## 7. Post Request to view create Bookings
![WhatsApp Image 2024-03-01 at 07 30 57_1fa4e0f0](https://github.com/Grg-Sid/Bipolar-Factory/assets/106266279/ff34240d-d1bf-4e8a-8b8c-92d096927b6b)

## Local Setup

1. Clone the repository:

```CMD
git clone https://github.com/Grg-Sid/Alemeno-task.git
```

2. Install, Create and activate a virtual environment:

```CMD
python3 -m venv .venv
```

Activate the virtual environment

```CMD
source .venv/bin/activate
```

3. Install the dependencies:

```CMD
pip install -r requirements.txt
```

5.Run the migrate command

```CMD
python manage.py migrate
```

6. Run the backend server on localhost:

```CMD
python manage.py runserver
```
