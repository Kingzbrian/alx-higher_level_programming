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
};

