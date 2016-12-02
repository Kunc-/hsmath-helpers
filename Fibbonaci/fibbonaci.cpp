#include <gmpxx.h>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>

int digits(mpz_class* m){
    return m->get_str(10).length();
}
int zeroes(mpz_class *m){
    std::string l = m->get_str(10);
    int last_zero = l.length();
    for (int i = 0; i < l.length(); i++){
        if (l[i] != '0') last_zero = l.length();
        else if (last_zero == l.length()) last_zero = i;
    }
    return l.length() - last_zero;
}

std::string make_string(int i){
    std::stringstream ss;
    ss << i;
    std::string out;
    ss >> out;
    return out;
}
int main(){
    int log_count = 1;
    std::time_t t = std::time(NULL);
    std::ofstream f ("num.txt", std::ofstream::out);
    mpz_class big_num_1 = 0;
    mpz_class big_num_2 = 1;
    mpz_class big_num_3 = 1;
    int limit = 500000;
    // std::cout << "Count to: ";
    // std::cin >> limit;
    for (int i = 2; i <= limit; i++){
        big_num_1 = big_num_2;
        big_num_2 = big_num_3;
        big_num_3 = big_num_1 + big_num_2;
        if (i % log_count == 0 || i < 1000){
            if (i == 10*log_count) log_count = 10*log_count;
            f << i << "th fibbonaci number = "<< big_num_3 << std::endl << "\n";
            std::cout << i << std::endl;
        }
        f << i << "th fibbonaci number " << "has: " << digits(&big_num_3) << " digits" << std::endl << "\n";
    }

    time_t diff_t = std::time(NULL);
    f << "Took (s): " << std::difftime(diff_t, t) << std::endl;
    f.close();

    return 0;
}
