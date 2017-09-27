package homework;

import homework.Outer;

public class TestOuter {
	public static final int HIGH = 10; // 代表随机数组范围[0,HIGH)
	public static final int SUM = 10; // 代表随机数组大小
	public static void showInfo() {
		System.out.println("数组的大小是："+SUM);
		System.out.println("数组的范围是：[0,"+HIGH+")");
	}
	public static void main(String[]args) {
		Outer outer = new Outer();
		Outer.Inner in = outer.new Inner();
		in.initArray(HIGH, SUM);
		showInfo();
		System.out.print("原始数组是：");
		outer.showArray();
		outer.sortArray(); // 数组进行快速排序
		System.out.print("排序后的数组是：");
		outer.showArray();
		System.out.println("最大的数是："+outer.getMax());
		System.out.println("最小的数是："+outer.getMin());
	}
}
