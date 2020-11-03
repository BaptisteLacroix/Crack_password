import time
import itertools
import pikepdf

caracteres_for_pdf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
file = "correction_TP_fractions.pdf"


def decrypt_password(nbr=4, count=0):
    for password in itertools.product(caracteres_for_pdf, repeat=nbr):
        password_found = "chap3_" + "".join(password)
        try:
            with pikepdf.open(file, password_found) as pdf:
                print("----------------------------")
                print("le mot de passe est : " + str(password_found))
                return True
        except:
            print(password_found, f"{count:_}")
            count += 1
            continue


def main():
    start = time.time()
    decrypt_password()
    end = time.time()
    print(round(end - start, 4), "Secondes")
    print(round((end - start) / 60, 2), "Minutes")
    print(round((end - start) / 3600, 2), "Heures")
    print("----------------------------")


if __name__ == '__main__':
    main()

# mdp correction recursivite : chap1_5330
# mdp correction poo : chap2_2966
# mdp correction bdd : chap3_0966
# mdp correction fraction : chap3_4415
# mdp correction Tp_Piles_Liste : 
