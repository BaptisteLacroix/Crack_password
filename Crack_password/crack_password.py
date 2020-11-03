import time
import itertools


class CrackPassword:

    user_pass = input("Enter your password : ")

    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O',
                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                  '9', '&', '~', '#', '"', "'", '{', '(', '[', '-', '|', '`', '_', "\\", '^', '@', ')', ']', '=', '}',
                  ' ', '¨', '^', '£', '$', '¤', '%', 'ù', 'µ', '*', ',', ';', ':', '?', '.', '/', '§', '!']

    caracteres_for_pdf = ['c', 'h', 'a', 'p', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.nbr = 1
        self.count = 0

    def all_permutations(self, r=None):
        """
        Génère toutes les permutations d'un itérable.
        :param r:
        :return:
        """
        # iterable = élément que l'on peut parcourir. Voir https://stackoverflow.com/a/9884259
        # Source : https://docs.python.org/fr/3/library/itertools.html#itertools.permutations
        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        # permutations(range(3)) --> 012 021 102 120 201 210 /
        pool = tuple(CrackPassword.caracteres)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                yield from self.all_permutations(r + 1)

    def verification(self):
        for permutation in self.all_permutations(self.nbr):
            self.count += 1
            print("".join(permutation), f"{self.count:_}")
            if "".join(permutation) == CrackPassword.user_pass:
                print("----------------------------")
                print(f"Nombres d'essaies : {self.count:_}")
                print("le mot de passe est : " + CrackPassword.user_pass)
                return permutation

    def verification2(self, nbr=1):
        for permutation in itertools.product(CrackPassword.caracteres, repeat=nbr):
            self.count += 1
            print("".join(permutation), f"{self.count:_}")
            if "".join(permutation) == CrackPassword.user_pass:
                print("----------------------------")
                print(f"Nombres d'essaies : {self.count:_}")
                print("le mot de passe est : " + CrackPassword.user_pass)
                return permutation
        self.verification2(nbr+1)


def main():
    crack_password = CrackPassword()
    start = time.time()
    crack_password.verification2()
    end = time.time()
    print(round(end - start, 4), "Secondes")
    print(round((end - start)/60, 2), "Minutes")
    print(round((end - start)/3600, 2), "Heures")
    print("----------------------------")


if __name__ == '__main__':
    main()
