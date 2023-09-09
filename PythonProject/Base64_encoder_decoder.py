import base64

print("############# Base64 Encoder & Decoder")

try:
    while True:
        user_input = int(input(''' \n Please choose the appropriate choices..:
        1 Base64 Encoder
        2 Base54 decoder
        3 Exit (Aside from 1 and 2, you can press any key for the exit.)
        '''))
        if user_input == 1:
            appid = input("Enter your Application ID: ")
            skey = input("Enter your seceret key: ")
            string_vl = (appid+":"+skey).encode("ascii")
            base64_byt = base64.b64encode(string_vl)
            base64_str = base64_byt.decode("ascii")
            print(f"\n Base64 Encoded String: {base64_str}")
        elif user_input == 2:
            base64_str = input("Enter the Base64 Encoded string: ")
            base64_byt = base64_str.encode("ascii")
            recv_str_byt = base64.b64decode(base64_byt)
            recv_str = recv_str_byt.decode("ascii")
            print(f"\n Base64 Decoded String: {recv_str}")
        else:
            break
except:
    print(" \n Exit")