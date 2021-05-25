import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom';

import './Courses.css';
import Course from '../Course/Course';


class Courses extends Component {
    state = {
        course: null,
        courses: [
            { id: 1, title: 'Angular - The Complete Guide' },
            { id: 2, title: 'Vue - The Complete Guide' },
            { id: 3, title: 'PWA - The Complete Guide' }
        ]
    }

    render () {
        let url = this.props.match.url;
        let courses = this.state.courses.map(course => (
            <Link
                key={course.id}
                to={{
                    search: `?title=${course.title}`,
                    pathname: `${url}/` + course.id }}>
                <article
                    key={course.id}
                    className="Course">{course.title}</article>
            </Link> ));

        return (
            <div>
                <h1>Amazing Udemy Courses</h1>
                <section className="Courses">{ courses }</section>
                <div>
                    <Route exact path={`${url}/:id`} component={Course} />
                </div>
            </div>
        );
    }
}

export default Courses;