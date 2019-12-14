#include <bits/stdc++.h>

int flaground[] = {30, 70, 101};

char buffer[666666];
long long d[100][222];

FILE *logfile;

void log(char *ch){
    fprintf(logfile, "%s", ch);
    fflush(logfile);
    fprintf(stderr, "|%s|\n", ch);
}

long long calc(long long r, long long k){
    long long res = 0;
    std::vector<int> vv;
    for (auto i = r; i; i /= 10){
        std::cout.flush();
        vv.push_back(i % 10);
    }
    long long last = 0;
    for (long long i = vv.size() - 1; i >= 0; i -- ){
        for (int j = 0; j < vv[i]; j ++ )
            if (k >= j + last)
                res += d[i][k - j - last];
        last += vv[i];
    }
    return res;
}

long long Main1(long long l, long long r, long long k){
    long long res = 0;
    for (auto i = l; i <= r; i ++ ){
        long long num = 0;
        for (auto j = i; j; j /= 10)
            num += j % 10;
        if (num == k)
            res ++ ;
    }
    return res;
}

void Main(){
    long long l, r, k, res;
    std::cin >> l >> r >> k;
    std::cerr << l << ' ' << r << ' ' << k << '\n';
    //auto trueres = Main1(l, r, k);
    res = calc(r + 1, k) - calc(l, k);
    //if (trueres != res) fprintf(stderr, "%lld %lld %lld %lld %lld\n", l, r, k, trueres, res);
    std::cout << res << std::endl;
}

void preprocess(){
    d[0][0] = 1;
    for (int i = 1; i <= 18; i ++ )
        for (int j = 0; j <= 9; j ++ )
            for (int k = 0; k < 200; k ++ )
                d[i][j + k] += d[i - 1][k];
    //for (int i = 1; i <= 18; i ++ )
    //    for (int j = 0; j <= 200; j ++ )
    //        d[i][j] += d[i - 1][j];
}

int main(){
    fprintf(stderr, "hello");
    preprocess();
    logfile = fopen("en1.out", "w+");
    gets(buffer);
    int nowflag = 0;
    for (int i = 1; i <= 999; i ++ ){
        fprintf(stderr, "%d\n", i);
        Main();
        if (i == flaground[nowflag]){
            getchar();
            gets(buffer);
            log(buffer);
            nowflag ++ ;
        }
    }
}