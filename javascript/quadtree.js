class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class Rectangle {
    constructor(x, y, w, h) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
    }

    contains(point) {
        return this.x <= point.x && point.x <= this.x + this.w &&
            this.y <= point.y && point.y <= this.y + this.w;
    }
}


class QuadTree {
    constructor(boundary, n) {
        this.boundary = boundary;
        this.capacity = n;
        this.points = [];
        this.divided = false;
    }

    insert(point) {
        if (!this.boundary.contains(point)) return;

        if (this.points.length < this.capacity) {
            this.points.push(point);
        } else {
            if (!this.divided) {
                this.subdivide();
                this.divided = true;
            }
            this.ne.insert(point);
            this.nw.insert(point);
            this.se.insert(point);
            this.sw.insert(point);
        }
    }

    subdivide() {
        const x = this.boundary.x,
            y = this.boundary.y,
            w = this.boundary.w,
            h = this.boundary.h;
        this.ne = new QuadTree(new Rectangle(x + w / 2, y, w / 2, h / 2));
        this.nw = new QuadTree(new Rectangle(x, y, w / 2, h / 2));
        this.se = new QuadTree(new Rectangle(x + w / 2, y + h / 2, w / 2, h / 2));
        this.sw = new QuadTree(new Rectangle(x, y + h / 2, w / 2, h / 2));
    }
}
