# prime number
n = int(input("Enter a number: "))
flag = True
if n > 1:                   # flag is just a variable, can check true/false 
    for i in range(2, n):   # if flag: directs the output when flag = true/false
        if (n % i) == 0:
            flag = False
            break             # break just stops loop not mandatory   
if flag == True:
    print(n, "is a prime number")   
else:
    print(n, "is not a prime number")
    
//Snake and ladder 

#include <iostream>
using namespace std;

class snake_ladder{
    public:
    int s_start;
    int s_end;
    int l_start;
    int l_end;
    int dice;
    public:
    void get_snakes(){
        cin>>s_start;
        cin>>s_end;
    }
    void get_ladder(){
        cin>>l_start;
        cin>>l_end;
    }
    void get_dice(){
        cin>>dice;
    }
};

int main(){
    snake_ladder s[100];
    int m,n;
    int no_snakes, no_ladder, no_dice;
    int col, row;
    cin>>m>>n;
    cin>>no_snakes;
    for (int i=0;i<no_snakes;i++){
        s[i].get_snakes();
    }
    cin>>no_ladder;
    for (int i=0;i<no_ladder;i++){
        s[i].get_ladder();
    }
    cin>>row>>col;
    cin>>no_dice;
    for (int i=0;i<no_dice;i++){
        s[i].get_dice();
    }
    int g=((row-1)*n) + col;
    for (int i=0;i<no_dice;i++){
        g=g+s[i].dice;
        for (int k=0;k<no_snakes;k++){
            if (s[i].s_end==g){
                g=s[i].s_start;
            }
        }
        for (int j=0;j<no_ladder;j++){
            if (s[i].l_start==g){
                g=s[i].l_end;
            }
        }
    }
    cout<<"Output: "<<endl;
    cout<<g;
    return 0;
}