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
std::string sci_not(mpz_class *m){
    int d = digits(m), z = zeroes(m);
    return m->get_str(10).substr(0, d-z) + "x10^" + make_string(z);
}

int main(){
    int log_count = 1;
    std::time_t t = std::time(NULL);
    std::ofstream f ("num.txt", std::ofstream::out);
    mpz_class big_int = 1;
    int limit = 10000000;
    // std::cout << "Count to: ";
    // std::cin >> limit;
    for (int i = 1; i <= limit; i++){
        big_int = i*big_int;
        if (i % log_count == 0){
            log_count = 10*log_count;
            f << i << "! = "<< sci_not(&big_int) << std::endl << "\n";
        }
        f << i << "! = " << "has: " << digits(&big_int) << " digits; and " << zeroes(&big_int) << " zeroes at the end.\n" ;
    }

    time_t diff_t = std::time(NULL);
    f << "Took (s): " << std::difftime(diff_t, t) << std::endl;
    f.close();

    return 0;
}
