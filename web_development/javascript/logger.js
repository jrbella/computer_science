
function diameter(raidus){

    return radius ** 2

}


const my_circle = (diameter) => {

    return 2*3.14*diameter
}


let radius = 10
let circle_value = my_circle(radius)
new_circle = my_circle(circle_value)

console.log(new_circle)