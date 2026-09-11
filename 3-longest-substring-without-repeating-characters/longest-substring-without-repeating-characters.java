class Solution {
    public int lengthOfLongestSubstring(String s) {
        StringBuilder sb = new StringBuilder(s);
        int max=0;
        for(int i=0;i<s.length();i++){
            int freq[] = new int[256];
            Arrays.fill(freq,0);
            for(int j=i;j<s.length();j++){
                if(freq[sb.charAt(j)]==1)
                break;
                freq[sb.charAt(j)]=1;
                if(j-i+1>max)
                max=j-i+1;
            }
        }
        return max;
        
    }
}