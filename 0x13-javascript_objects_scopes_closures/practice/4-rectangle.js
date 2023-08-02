#!/usr/bin/node
module.exports =  class Rectangle{
        constructor (w, h){
                this.width = w;
                this.height = h;
                if (isNaN(h) || isNaN(w) || h <= 0 || w <= 0 )
                {
                        const obj = {};
                        return(obj);
                }
        }
        print()
        {
                for(let i = 0; i < this.height; i++) console.log('x'.repeat(this.width))
        }
	rotate()
	{
		let a = this.width;
		this.width = this.height;
		this.height = a;
	}
	double()
	{
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
};
