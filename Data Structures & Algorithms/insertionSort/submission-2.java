// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        if (pairs.size() == 0) {
            return new ArrayList<>();
        }
        List<List<Pair>> res = new ArrayList<>();
        res.add(new ArrayList<>(pairs));
        for (int i = 1; i < pairs.size(); i++) {
          Pair temp = pairs.get(i);
          int j = i - 1;
          while (j >= 0 && pairs.get(j).key > temp.key) {
            pairs.set(j + 1, pairs.get(j));
            j--;
          }  
          pairs.set(j + 1, temp);
          res.add(new ArrayList<>(pairs));
        }
        return res;
    }
}
