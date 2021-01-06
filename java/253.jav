class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int len = intervals.length;
        int[] startTime = new int[len];
        int[] endTime = new int[len];
        int index = 0;
        for(int[] interval: intervals){
            startTime[index] = interval[0];
            endTime[index++] = interval[1];
        }
        Arrays.sort(startTime);
        Arrays.sort(endTime);
        int i = 0, j = 0;
        int activate = 0, max = 0;
        while(i < len && j < len){
            if(startTime[i] < endTime[j]){
                activate++;
                i++;
            }else{
                activate--;
                j++;
            }
            max = Math.max(max, activate);
        }
        return max;
    }
}

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if(intervals.length <= 1) return intervals.length;
        int result = 1;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b)->{
            return a[1] - b[1];
        });
        Arrays.sort(intervals, (a, b)->{
            return a[0] != b[0] ? a[0] - b[0]: a[1] - b[1];
        });
        pq.offer(intervals[0]);
        for(int i = 1; i < intervals.length; i++){
            if(intervals[i][0] >= pq.peek()[1]){
                pq.poll();
            }
            pq.offer(intervals[i]);
            result = Math.max(result, pq.size());
        }
        return result;
    }
}