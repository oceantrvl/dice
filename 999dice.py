B
    X5]1,  �               @   s   d dl Z ee �d�� dS )�    Ns3  �            	   @   s<  d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZmZmZ ej	dd� e
dd��Ze�� ZW dQ R X e�e�Zeed d �d	 Zeejej d
 ej ej d ej ej d ej ej d ej d ej ej d ej ej d ej d ej ej d ej ej d ej ej d ej ej d ej ej d ej ej d ej ej d ej ej d ej d ej ej d ej d ej ej d ej d � ejej ZejZejej Zejej Zejej Zejej Z e �!� Z"dZ#dd d!d"d#d$d%�Z$eed d& �d' Z%ee&ed( �d) �Z'd*d+� Z(e"j)e#e$d,d-ed. d/ ed. d0 d1d2�d3�Z*e�e*j+�Z,y4eed4 e d e e-e&e,d5 d6 �d) � � W n   ed7� e�.�  Y nX e&e,d5 d6 �d) e&d8�k�reed9 � e�.�  e(ee&ed: �d) �ee&ed; �d) �� dS )<�    N)�Fore�Back�StyleT)Z	autoresetzconfig.json�r�ConfigZIntervali�  z�      ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/z)
=======================================
zAuthor By  z: zKadal15
zChannel Yt �:z Jejaka Tutorialz
999 Dice Botz | zLose Streak �|z Win Streak
zDonate z BTC z#18961sqv9fPuBcEbbi1gHub8ydWePB8yaG
z         LTC z#LNRkk6o9h1Rh98sDW8byeH9HbeUHwNohDu
z         Doge z$DJG4YG3ARUkSt9e5xvHvSS3faVx3v1HM9p

z$https://www.999doge.com/api/web.aspxzfile://z�Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36z!application/x-www-form-urlencodedz*/*z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7zcom.reland.relandicebot)ZOriginz
user-agentzContent-typeZAcceptzAccept-LanguagezX-Requested-WithzReset If Win�   ZBeti ��c          	   C   sf  t }dtd |td d td d td ddd	�}�y�tjtt|d
�}t�|j	�}|d t
|d � t
|� }t
|d �t
|� }t|d t
|d � t
|� | �d }ttd tttt
|d �t
|� �d � � d}	d}
�xLt�tt�� t
|�}|	d7 }	dtd |td d td d td ddd	�}|ttd �k�rjttd t d t t|� � t��  tjtt|d
�}t�|j	�}t|d t
|d � t
|� | �d }t
|d �t
|� }|d | k�r6ttd t tt|�d � tttt
|d �t
|� �d � td tt|� � ttd � t��  |d |k �r�ttd t d tt|�d � tttt
|d �t
|� �d � td tt|� � ttjtj d � t��  |d dk	�rtt
|d �t
|� �d td�k�rPttd t tt|�d � tttt
|d �t
|� �d � td tt|� � ttd � t��  |dk�r�ttd t tt|�d � tttt
|d �t
|� �d � td tt|� � nRttd t tt|�d � tttt
|d �t
|� �d � td tt|� � n�d}d}
|dk�rlttd t d tt|�d � tttt
|d �t
|� �d � td tt|� � nVttd t d tt|�d � tttt
|d �t
|� �d � td tt|� � |
dk�r |d7 }t
|�ttd d  � }|tk�r,d}d}
q�|	tk�rd}	t }q�t
|�ttd d! � }q�W W n.   yt|d" d# � W n   Y nX Y nX d S )$NZPlaceBetZSessionCookieZChance�Low�High�
ClientSeedZdoge�2)�a�sZPayInr
   r   r   ZCurrencyZProtocolVersion)�headers�dataZStartingBalanceZPayOuti ��z


Starting Balancer   Fr	   zTarget Profitz$Yay.! 
Profit Mencapai Target.....!
zProfit z	[Status] ZProfitz)Yay.!
Balance Sudah Memenuhi Target.....!z[Status]�-zLose zLose Target....!g     @@zzMaaf Versi Ini Cuma Support Untuk Balance Dibawah 500 Doge
Silahkan Hubungi Author Untuk Full Version
Hub : +6285336117892Tr   zIf LosezIf WinZInsufficientFundszInsufficientFunds
)�payin�js�obj�cZpost�url�ua�json�loads�text�int�float�print�hijau�res�str�timeZsleep�slp�sys�exit�ungu�hijau2�red2r   �BRIGHTr   �RED�limit_a)ZwsZlsZamountr   Zr1ZjsnZjumblZjumZprof�nZburst�i� r.   � �dice(   s�    

(.

 (RV&R
TT
XV


 r0   ZLoginZ 7ec7f8a2c9724b2cbb8ed75e72b47ee9ZAccount�Username�Passwordr/   )r   ZKeyr1   r2   ZTotp)r   r   zBalance ZDogeZBalancez%Check Your Username And Your Passwordg     @@z|

Maaf Versi Ini Cuma Support Untuk Balance Dibawah 500 Doge
Silahkan Hubungi Author Untuk Full Version
Hub : +6285336117892z
Target WinzLose Target)/Zrequestsr   r"   r$   ZrandomZcoloramar   r   r   Zinit�openZmyfile�readr   r   r   r   r#   r   ZNORMALZMAGENTAZGREENr)   ZDIMZWHITEZ	RESET_ALLr*   r   r    Zabu2r&   r'   r(   Zsessionr   r   r   r+   r   r   r0   �getr   r   r   r!   r%   r.   r.   r.   r/   �<module>   sJ   (
� 7X,4)�marshal�exec�loads� r   r   �out.py�<module>   s   