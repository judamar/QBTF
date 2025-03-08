English | [Español](key_tuto-es.md)

# Tutorial

1. Open [Firebase](https://console.firebase.google.com/u/0/), sign in with Google, and click on `Add project`.
2. Give your project a name, click `Continue`, then `Continue` again on step 2. In step 3, select `Default account to Firebase` and click `Create project`.
3. Open your project and, in the right panel, find `Storage` and open it.
4. Click `Get Started`, then `Next`, and finally `Done`.
5. Once created, at the top you will see something like this. Click on `Rules`.

[![st-rules.png](https://i.postimg.cc/3r9Rp1qc/st-rules.png)](https://postimg.cc/w3ygYXgX)

6. In the Edit Rules section, change `allow read, write: if request.auth != null;` to `allow read, write: if true;` and click `Publish`.

[![allow-true.png](https://i.postimg.cc/VLpzBVWD/allow-true.png)](https://postimg.cc/qzcfpQY3)

7. Go back to your project's overview and click on `</>` WEB, register the app without checking anything. A configuration file will appear.

[![overview.png](https://i.postimg.cc/9Xk6vqwf/overview.png)](https://postimg.cc/w3h4NMVK)

8. Copy the contents of the `firebaseConfig` variable and paste it into the same variable inside the plugin's configuration file, but formatted as a [dictionary](https://youtube.com/clip/Ugkxc8d-DNlt49jpA5VZ0sw9pmpYBv2ZX1xx), meaning each key and value inside `""`, keeping the last key (`"databaseURL": ""`). Then, click Continue to the console.

[![key.png](https://i.postimg.cc/76jyMCgb/key.png)](https://postimg.cc/G8PNbmg1)

Now, you can run the plugin correctly.
