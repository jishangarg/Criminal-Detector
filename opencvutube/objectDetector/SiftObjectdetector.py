import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'getSubsets' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER k
     *  2. INTEGER n
     *  3. INTEGER_ARRAY arr
     */

    public static int getSubsets(int k, int n, List<Integer> arr) {
        int mod=1000000;
        int mod2=1000000007;
        int sum=0;
        for(int i=0;i<arr.size();i++)
        {
            int temp=arr.get(i);
            for(int j=2;j<=arr.get(i);j++)
            {
                if(temp%j==0)
                {
                    sum=(int)((sum%mod+j%mod+0l)%mod);
                    temp=temp/j;
                    j--;
                }
            }
            // System.out.println(sum);
        }
        // System.out.println(sum);
        return (findWays(sum,k,mod2))%mod2;



    }
    public static int findWays(int sum,int k,int mod2)
    {
        int[]dp=new int[sum+1];
        for(int i=0;i<=sum;i++)
        {
            dp[i]=1;
        }
        for(int i=2;i<=k;i++)
        {
            dp[0]=1;
            for(int j=1;j<=sum;j++)
            {
                dp[j]=(dp[j-1]%mod2+dp[j]%mod2)%mod2;
            }
        }
        return dp[sum]%mod2;

        // int ans=0;
        // if(k==1)
        // {
        //     return 1;
        // }

        // for(int i=sum;i>=0;i--)
        // {
        //     ans=(ans+findWays(i,k-1,mod2)%mod2)%mod2;
        // }
        // return ans%mod2;
    }

}

public class Solution {