from selenium import webdriver
import time
browser=webdriver.Chrome()  
browser.get('https://www.codechef.com') 
username=browser.find_element_by_id("edit-name")
username.send_keys("adity_8726")
password=browser.find_element_by_id("edit-pass")
from getpass import getpass
password.send_keys(getpass("enter Password:"))
browser.find_element_by_id("edit-submit").click()
browser.get("https://www.codechef.com/submit/RGAME")
time.sleep(10)
browser.find_element_by_xpath('//*[@id="edit_area_toggle_checkbox_edit-program"]').click()
#with open("solution.cpp","r") as f:
    #code=f.read()
code_submit=browser.find_element_by_id("edit-program")
code_submit.send_keys("""
    #include <bits/stdc++.h>
    #include <iostream>
    #include <vector>
    #include <queue>
    #include <algorithm>
    #include <stack>
    #include <iomanip>
    #include <fstream>
    #include <string>
    #include <cstdlib>
    #include <utility>
    #include <ctime>
    #include <cmath>

    using namespace std;

    typedef long long ll;
    typedef unsigned long long ull;
    #define fi first
    #define sec second
    #define FOR(s,e) for(ll i=s;i<e;i++)
    #define MOD 1000000007

    void solve();

    int main() {
        ios::sync_with_stdio(0);
        cin.tie(NULL);
        ll t;
        cin >> t;
        while(t--)
            solve();
        return 0;
    }

    void solve(){
        ll n;
        cin >> n; n++;
        ll arr[n];
        FOR(0,n)
            cin >> arr[i];
        ll ans=0,p=1,k=2*arr[0];
        FOR(1,n){
            ans=(2*ans+k*arr[i])%MOD;
            p=(p*2)%MOD;
            k=(k+arr[i]*p)%MOD;
        }
        cout << ans << endl;
    }
    """
)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="edit-submit-1"]').click()

