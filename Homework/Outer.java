package homework;

import java.util.ArrayList;
import java.util.Random;
import java.util.Comparator;

public class Outer {
	private ArrayList<Double> random_array;
	class Inner {
		public void initArray(int high,int sum) { 
			/**
			 * high:范围
			 * sum:生成的随机数的总个数
			 */
			random_array = new ArrayList<Double>();
			Random rand = new Random();
			for(int i=0;i<sum;++i) 
				random_array.add(rand.nextDouble()*high);
		}
	}
	public void showArray() {
		if (random_array.size()!=0) // 数组已经初始化
			System.out.println(random_array);
		else //当数组没有初始化
			System.out.println("请调用内部类初始化随机数组");
	}
	protected void sortArray() { // 使用快速排序，时间复杂度是O(logN)，大大优于传统的一位位检索
		random_array.sort(new Comparator<Double> () {
			@Override 
			public int compare(Double a,Double b) {
				return (a<b)?-1:1;
			}
		});
	}
	public Double getMax() {
		return random_array.get(random_array.size()-1);
	}
	public Double getMin() {
		return random_array.get(0);
	}
}
