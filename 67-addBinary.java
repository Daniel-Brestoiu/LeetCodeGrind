class Solution67 {
    public String addBinary(String a, String b) {
        int lenA = a.length();
        int lenB = b.length();
        
        int maxSize = Math.max(lenA, lenB);
        int minSize = Math.min(lenA, lenB);
        char[] result = new char[maxSize];
        
        boolean carry = false; 
        for (int i = 0; i < maxSize; i++) {
            if (i >= minSize) {
                //0 as storage value.
                char c = 0;
                if (i >= lenA) {
                    c = b.charAt(lenB - 1 - i);
                } else if (i >= lenB) {
                    c = a.charAt(lenA - 1 - i);
                }

                if (c == '0') {
                    result[maxSize - i - 1] = carry ? '1' : '0';
                    carry = false;
                } else {
                    result[maxSize - i - 1] = carry ? '0' : '1';
                }
            } else if (a.charAt(lenA - 1 - i) == '0' && b.charAt(lenB - 1 - i) == '0') {
                result[maxSize - i - 1] = carry ? '1' : '0';
                carry = false;
            } else if (a.charAt(lenA - 1 - i) != b.charAt(lenB - 1 - i)) {
                char value = carry? '0' : '1';
                result[maxSize - i - 1] = value;
            } else {
                //Both are one. Carry over.
                char value = carry ? '1' : '0';
                result[maxSize - i - 1] = value;
                
                carry = true;
            }
        }
        
        //Consider case of carry on last digit. One str longer.
        if (carry) {
            char[] result2 = new char[maxSize + 1];
            result2[0] = '1';
            for (int i = 0; i < result.length; i++) {
                result2[i + 1] = result[i];
            }
            result = result2;
        }
        
        String strResult = new String(result);
        return strResult;
        
    }
}