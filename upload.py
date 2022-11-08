import requests
import hashlib
import json
import time
from pathlib import Path


innertube_studio = "xxxxxxx-2D50-4xx3-9C28-8xxxxxx0A69F:0"
uploadID = {"frontendUploadId":"innertube_studio:" + innertube_studio}

filename = 'xxxxxxxxxxxxx.mp4'
filesize = Path(filename).stat().st_size

channel = "xxxxxxxxxxxxxxxxxxxxx"
privacy = "PRIVATE"
draft = "true"

initurl = 'https://upload.youtube.com/upload/studio?authuser=0'
initheaders = {
    "authority": "upload.youtube.com",
    "method": "OPTIONS",
    "path": "/upload/studio?authuser=0",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "access-control-request-headers": "x-goog-upload-command,x-goog-upload-file-name,x-goog-upload-header-content-length,x-goog-upload-protocol",
    "access-control-request-method": "POST",
    "origin": "https://studio.youtube.com",
    "referer": "https://studio.youtube.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106",
}

initAuth = requests.options(url = initurl, headers = initheaders)

print(initAuth.headers)
print('\n')

SAPISID = "xxxxx26Qu7AExxxxxiQH0zFhxxxx"
LOGIN_INFO = "xxxxxRAIgLllxbd5dCMOuFXjlew1xRRqSxxxxm7nT3uq6U8CIDzu-IANykq9C_Qw5rffC0ckI--aj3SopSPCxxxxxeFU2bWQ2cXl6ZlVwY3UzM2R3dmdsY0pFRmI5QkxYTDdOS2FoTHR0TxxxxxUW1VYXU4cXRodUc0MWZyN1llbW5YNXlOczBfcUhRYxxxxxxdMdzJwMkNIOXRGQ3RJc3g2NDAxxxxRnpsbTVQemVhMlFjOXxxxxxl6TDV3X0Jxxxxxxxxxxxx"
VISITOR_INFO1_LIVE= "xx2hRF7Axxxxx"
YSC="xxHDxxxLCxxx"
HSID="xxzRxYPBCrcxxxxxx"
SSID="xxxxxx6sUurx"
APISID="xP6u1vrxxxxxm99Fdxxxxxx"
wide="0"
PREF="tz=Africa.Johannesburg&f6=40000000&f5=20000&f7=100"
SID="xxxxxQ4rAAwThwAfwdA0_EWklS-9s6xxxxxqc0SlJxeuTxxxxxx"
Secure1PSID="xQ4rAAwThwAfwx-9s6D940STL9HLExxxHVDZKqw1x"
Secure3PSID="xQ4rAAwThwAfwxLKTIAbPxxcy-xxxx"
SIDCC="xuyO-PdxybxlJxx"
Secure1PSIDCC="xJpk7lqmwm4nUEUxz5cx"
Secure3PSIDCC="AIKkxcHttw9e0cPvRGx"
    



authUrl = 'https://upload.youtube.com/upload/studio?authuser=0'
authHeaders = {
    "authority": "upload.youtube.com",
    "method": "POST",
    "path": "/upload/studio?authuser=0",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "78",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "cookie": "VISITOR_INFO1_LIVE=" + VISITOR_INFO1_LIVE + "; YSC=" + YSC + "; HSID=" + HSID +"; SSID=" + SSID +"; APISID=" + APISID + "; SAPISID="+ SAPISID +"; __Secure-1PAPISID="+ SAPISID +"; __Secure-3PAPISID="+ SAPISID +"; LOGIN_INFO=" + LOGIN_INFO + "; wide=" + wide + "; PREF=" + PREF +"; SID=" + SID + "; __Secure-1PSID=" + Secure1PSID + "; __Secure-3PSID=" + Secure3PSID + "; SIDCC=" + SIDCC + "; __Secure-1PSIDCC=" + Secure1PSIDCC + "; __Secure-3PSIDCC=" + Secure3PSIDCC,
    "origin": "https://studio.youtube.com",
    "referer": "https://studio.youtube.com/",
    "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Opera GX\";v=\"91\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"105.0.5195.127\"",
    "sec-ch-ua-full-version-list": "\"Opera GX\";v=\"105.0.5195.127\", \"Not)A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"105.0.5195.127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106",
    "x-goog-upload-command": "start",
    "x-goog-upload-file-name": filename,
    "x-goog-upload-header-content-length": filesize,
    "x-goog-upload-protocol": "resumable"
  }

studioAuth = requests.post(url = authUrl, headers = authHeaders, json = uploadID)

print(studioAuth.headers)
print('\n')



uploadINFO = dict(studioAuth.headers)

origin = "xNvbS91cGxvYWQvc3R1ZGlvEhxibGxxxxC12aWRlby11cGxxxxxx"

print(uploadINFO['X-GUploader-UploadID'])
print(uploadINFO['X-Goog-Upload-Header-Scotty-Resource-Id'])

tempurl = 'https://upload.youtube.com/?authuser=0&upload_id='+uploadINFO['X-GUploader-UploadID']+'&upload_protocol=resumable&origin='+origin


tempheaders = {
    "authority": "upload.youtube.com",
    "method": "OPTIONS",
    "path": "/?authuser=0&upload_id="+uploadINFO['X-GUploader-UploadID']+"&upload_protocol=resumable&origin=" + origin,
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "access-control-request-headers": "x-goog-upload-command,x-goog-upload-file-name,x-goog-upload-offset",
    "access-control-request-method": "POST",
    "origin": "https://studio.youtube.com",
    "referer": "https://studio.youtube.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106",
  }

tempAuth = requests.options(url = tempurl, headers = tempheaders)
print(tempAuth.headers)
print('\n')

videoKey = "xxxxetSUmoZxxxx5Xinxxxxxx"


createVideoUrl = 'https://studio.youtube.com/youtubei/v1/upload/createvideo?alt=json&key=' + videoKey


#https://subdomain.google.com

visitorid = "xxx0EyZyxxxxx%3D%3D"
delegationcontext = "ExxxxxxxaZGZCaUNxxxxx"
pagecl = "xxxxxxxx"
clientname = "xx"
clientversion = "1.20221102.02.00"
token = "xxxxw_GYe58gbkiFKxh7ay9MZv3R4xxxxxosZJLnwW41OIMKCuuAx5y9T1EGsIv7rxxxxxxP4YKmiFBGxxxxxx=="

experimentsToken = ""
utcOffsetMinutes = "120"
userInterfaceTheme = "USER_INTERFACE_THEME_DARK"
screenWidthPoints = "2519"
screenHeightPoints = "1337"
screenPixelDensity = "1"
screenDensityFloat = "1"
clientScreenNonce = "xxxxUyMDQwMjxxxxx"


SAPISIDHASH = hashlib.sha1(' '.join([str(int(time.time())), SAPISID, 'upload.youtube.com']).encode()).hexdigest()

#botguardKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdswdKYEslCfDAKONbUM6O2445R95p4AAAAqzgAAABj0AQcFBX10CuQK7c-Yh3S9OV6NOZ1vICVhpBdZ8cM1g0YPUI7JZtFydsWFrKaEpnTv8UMP9Bk_F-sWEv-LZz1MujgZmv6yMiJqMbNtL82Zn5iPaVQipt56dUHuDK6kFhGBHG2AAqic6YUYCaodJNuxvoXyjjfrn27XNkkHB1t0cVee7wtopfIZqBZ4bVyGPN21S_-bPvn1W7m0niNrIxh9nl9ERBkAIG6Rv78GoZDi3IU72Fzb8mRQ8t99f16zdcfKr_ja7mMNKbytzEHZhweEHWdMPNfXGLdKfglYO0keyVn1tOf4F5sLXhEsEZIKR0Y6pAjN354223xcAHVunxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-W5ox10cv9EIFKWdXU3Q9LajgPSPCqODggzRqZi0h_B69nYfWed8W2aUoCwefEag56uZGWdqqI8iaTUhS3U948oFcKCU0TCX5b1BjwRfF4WQJrOBFHxJhjXovvWszFlrJRrVP7PH1BGWZJ_MUKQihPJ2U0Ngfi9rPAUc6e5p0gRG8htUAKI8dp1DhgSY1QGTytG6M1mi4Cf45cEWZ-x-JZPpuiJJ6VXL_5CmstmegT44fV1lW0RLScXpJjP5Qgm6pEi48Cv_8Md-0okt-eKFJB_WBM6hYoHSqeoNAbL-45Q4gS4inHOeduGPco2kWQ0hkRoY-lT2ZOHsLp-qsX3RS6eDy2YSiuHIwCfINVS6AAk-LjKhWEf58DEPgqJuocPhLAJ8X9WI3fNAqrW5eMogrrV0naQJ_dOwKdGOCw-CmH8bx91lhmGoHpWKbZ1zR34Lfi-copFiDgnIccBfUVdxgfmKgvwUDSuv3i1ZfV2Ba5sYDMl7nyfJlrdsEoZPHAL3rQHsc0jz19QrNHZsMPhtExxxxxxxx5w3q9Une74d6FnhdmoenHHZe_Gqef8WYiU_b_VH-ZKlRK3yCK0yuGbpyDnXeHGzQzNAC6OegxxxPwjT9T4ywYjowrz8ap05zWQPJNxL2bJcnh0_f7ZSJc-taMQklipyM-YfPBeVyVCNujJ5BIWbYis-jHmmNlG9a4Vuq5DIMR6lsXB3ZwZjfCtj0H7pevQEhwRctI5KJnxd5u4oyxdRrx1kQpIGINsDJ43KhBExaQCOinehSTgAhxu-0rMqjhal498M9gAiW4kk23UHpjevG_5Qda7j0VR1IJQs_K5VOx8Nv6ciqmuRUIlJqr61WBLofzPAxuqS9eqD9JvepEhgKRlaUad7vpGOnl1ZnDFAD50fPxTnfLsPFsKQZaYMTaz75QBDRXqn4OdxI3Z8HrpGby3GMofTajc9z3VqIUQTBMpc5pzKoWuvOSJiyjK9ThDkxCRtcL89da9llkaQRuTTJDI0fNuelOzDYA6dGf7cc4u3sQUAloU4Qv6s3yP3JZry4WvXAu9IOc1JPJtyHUrmaxxxxxxx1lsqxuwEq3ARhqAyj93QRaN00zYaWiZOxYMbuuQjF2idUXWI1q21RSu165F5EDI7zFGQ_hDESkt2Eduhwpzz7-s3cT4XJrNbTZ5KEFl0ZxGtZb6o1bDzN9b08rKqaREl9L0fi5W5OjlUXbMm4AwqXmZhwowwsSFX9eGjyjFT1ui7fjPFQOkuYN-MEtJXmOLHOzKEYmncG4752n6Tc5wShKJXmAJFLkvpO5lUQUm1xbbszacyHGgNCwinwBOc1A1V-FpJkjDD8v5n3ecBpjKwHls_KxtImvI5lUAsq2vWT4lJxz0KnPB-D'
botguardKey = '<ToJqgs8CAAZEaxxxxxxxxxxxCMLJYZKr9wL9DdC2wHkhVTfQj50SSzZ95n0fb8Ew5M0AAABInQAAAASnAQdWBSaYFDWak-oxOTeHYbx9uKcDDHWeCMotKwA9Nv5zqhLZG6cC2Tl3ROkQfqA5R0pwBdV5VpQfVhggXHMVSEVHwfm9jceVnwLslV4iMhEeP0BiBU2Nx78HkIsuqcF-YhCAXaKGNRgtHQir5q4eeBIWdnHY2q5FCwcpuQ8qNadyFgXz8toSg39VKaWgSrLdx6_l6VvYWeRt7-Y6tYaG_iSI1pCvwkhj8yoVv4KVn2_cb-AOC9ni5YS_TPqhKBF7A3nkJbCYb2O-KQCxQabSIcpUJIidZydugMTsTlnAznPTI7vScWm5Xq2cxIMXIio3DgGjloYAyU05p_u0AKpR54TAS_nBgw9RDr2x2AjVvFjVe92DM7y6awq1c6P0d80fp-k7eJUm_bBytppwO-4_D8XDUVkS3sa9kmI9_aG1XT39bmD6OeTgKYRZYV2mcvAw1s9J7ecEjGkV7k4BQzHYSS-xRSfQadOyJOA4-dBpVYl9ai84Tvitds0KXLIduQoW0_9W0mf20H-YahaDWaeS837HVKbPTbzPH39da3yRlfNPOVb5CJVkXdaZlU86Dsg77qenfF7E6dyzfyz7W7WTiJGhdEKz_HbouEU_0TbFDnmJO8bWixU14fWv4IdgKaHuV1s9tA4M57AAHKtO4CKjuZhzw40Gqce3vpV8fjS1S6iHCl88aBhEaM8xd5sWzqmA53LlFPBGECVbXPAASigMCHq1Hi6IgmpGapF_hXQSXBdz9pB82Puk48pgmAveWqCScrRYntiX-N4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd1oAO3QClMk-zBjfIVsrxGlHtfp2NeoTBZ4r2vTHxP1iCjAwDu-hL6M1EwF-4_Ub22yItPzGHYE8oKv_kRbxMdtsNOGg8mX5ca3MhEDT86n2MVS74tgQzwQ78nDIJXgm4M42KAlZ-uquJ1iZEUcJqHe-Br6Be_3hjDPneDEiDfOaDbayXXBSHw6csgRfqXSBZfbZzDnhmqWGv0MwOYwcZacMvdRCDYHHy586vTvtE1TXXquPWL12RISiLH4srYT8UvN1dQvB2Zb2wz3Q2jyBg8TeHEkbRgPNLob0rNQ8brwHwfunrAA_i54XRdcLZiWKuKB704Y44N-DPGkQk10aeEwOf7zFpk2-WxXGEE57AfwqviIyVCILdDWIS1xSGutyxLU5q5DKoLZLJcCazwi_onKJt_kAmH2qjmqwDu2DlBnLIUAylkkejCt1F2ZL_34IaqSQXroU8VdU6ANauSo-6xQBXYCneCxfqzUIasJnVa_Yeo-8LYtFJmrQIFjQS0NfutM8UpWcF0d3lQOvd18TUMeM3SwJ8-m_QBfA2me1oYNE3sNprAW8zdcc8fNltSy_9SXnW0wCK6HN-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
createVideoHeaders = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "SAPISIDHASH" + SAPISIDHASH,
    "content-type": "application/json",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-goog-authuser": "0",
    "x-goog-pageid": "undefined",
    "x-goog-visitor-id": visitorid,
    "x-origin": "https://studio.youtube.com",
    "x-youtube-ad-signals": "dt=1667578872971&flash=0&frm&u_tz=" + utcOffsetMinutes + "&u_his=2&u_h=1440&u_w=2560&u_ah=1440&u_aw=2560&u_cd=24&bc=31&bih=" + screenHeightPoints + "&biw=" + screenWidthPoints + "&brdim=0%2C0%2C0%2C0%2C2560%2C0%2C2560%2C1440%2C" + screenWidthPoints + "%2C" + screenHeightPoints + "&vis=1&wgl=true&ca_type=image",
    "x-youtube-client-name": clientname,
    "x-youtube-client-version": clientversion,
    "x-youtube-delegation-context": delegationcontext,
    "x-youtube-page-cl": pagecl,
    "x-youtube-page-label": "youtube.studio.web_" + clientversion.split(",")[1] + "_" + clientversion.split(",")[2] + "_RC" + clientversion.split(",")[3],
    "x-youtube-time-zone": "Africa/Johannesburg",
    "x-youtube-utc-offset": "120",
    "cookie": "VISITOR_INFO1_LIVE=" + VISITOR_INFO1_LIVE + "; YSC=" + YSC + "; HSID=" + HSID +"; SSID=" + SSID +"; APISID=" + APISID + "; SAPISID="+ SAPISID +"; __Secure-1PAPISID="+ SAPISID +"; __Secure-3PAPISID="+ SAPISID +"; LOGIN_INFO=" + LOGIN_INFO + "; wide=" + wide + "; PREF=" + PREF +"; SID=" + SID + "; __Secure-1PSID=" + Secure1PSID + "; __Secure-3PSID=" + Secure3PSID + "; SIDCC=" + SIDCC + "; __Secure-1PSIDCC=" + Secure1PSIDCC + "; __Secure-3PSIDCC=" + Secure3PSIDCC,
    "Referer": "https://studio.youtube.com/channel/" + channel + "/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}


createVideoPayload = {
    "channelId": channel,
    "resourceId":{
        "scottyResourceId":{
            "id": uploadINFO['X-Goog-Upload-Header-Scotty-Resource-Id']
        }
    },
    "frontendUploadId":uploadID,
    "initialMetadata":{
        "title":{
            "newTitle": filename.split(".")[0]
        },
        "privacy":{
            "newPrivacy": privacy
        },
        "draftState":{
            "isDraft": draft
        }
    },
    "botguardClientResponse":botguardKey,
    "context":{
        "client":{
            "clientName":clientname,
            "clientVersion":clientversion,
            "hl":"en-GB",
            "gl":"ZA",
            "experimentsToken": experimentsToken,
            "utcOffsetMinutes": utcOffsetMinutes,
            "userInterfaceTheme": userInterfaceTheme,
            "screenWidthPoints": screenWidthPoints,
            "screenHeightPoints": screenHeightPoints,
            "screenPixelDensity": screenPixelDensity,
            "screenDensityFloat": screenDensityFloat
        },
        "request":{
            "returnLogEntry":"true",
            "internalExperimentFlags":[],
            "sessionInfo":{
                "token": token
            }
        },
        "user":{
            "delegationContext":{
                "externalChannelId": channel,
                "roleType":{
                    "channelRoleType":"CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                }
            },
            "serializedDelegationContext": delegationcontext
        },
        "clientScreenNonce": clientScreenNonce
    },
    "delegationContext":{
        "externalChannelId": channel,
        "roleType":{
            "channelRoleType":"CREATOR_CHANNEL_ROLE_TYPE_OWNER"
        }
    }
}

createVideo = requests.options(url = createVideoUrl, headers = createVideoHeaders, data = createVideoPayload)
print(createVideo.headers)
print('\n')
print(createVideo.content)