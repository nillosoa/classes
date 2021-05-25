import React, { Component } from 'react';

class Course extends Component {

    state = {
        courseId: null,
        courseTitle: null
    }

    componentDidMount () {
        this.courseHandler();
    }

    componentDidUpdate () {
        this.courseHandler();
    }

    shouldComponentUpdate ( nextProps, _ ) {
        return this.state.courseId !== +nextProps.match.url.split('/').slice(-1)[0];
    }

    courseHandler () {
        this.setState({
            courseId: +this.props.match.url.split('/').slice(-1)[0],
            courseTitle: new URLSearchParams(this.props.location.search).get('title') });
    }

    render () {
        return (
            <div>
                <h1>{ this.state.courseTitle }</h1>
                <p>You selected the Course with ID: { this.state.courseId }</p>
            </div>
        );
    }
}

export default Course;