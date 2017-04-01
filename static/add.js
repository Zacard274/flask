/**
 * Created by guangyang on 2017/3/28.
 */
function add() {
    var adder1 = Number(document.form1.add1.value);
    var adder2 = Number(document.form1.add2.value);
    var sum = adder1+adder2;
    alert(sum);
    document.form1.sum.value = sum;
}