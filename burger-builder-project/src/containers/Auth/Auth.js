
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom';

import classes from './Auth.css';
import Input from '../../components/UI/Input/Input';
import Button from '../../components/UI/Button/Button';
import Spinner from '../../components/UI/Spinner/Spinner';
import * as actions from '../../store/actions';
import { updateObject, checkValidity } from '../../shared/utility';


class Auth extends Component {

  state = {
    controls: {
      email: {
        value: '',
        valid: false,
        validation: {
          isEmail: true,
          required: true
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'email',
          placeholder: 'Mail Address'
        }
      },
      password: {
        value: '',
        valid: false,
        validation: {
          minLength: 6,
          required: true
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'password',
          placeholder: 'Password'
        }
      }
    },
    isSignup: true
  }

  componentDidMount () {
    if (!this.props.buildingBurger
      && this.props.authRedirectPath !== '/') {
      this.props.onSetAuthRedirectPath();
    }
  }

  inputChangedHandler = (event, controlName) => {
    const updatedControls = updateObject(
      this.state.controls, {
        [controlName]: updateObject(
          this.state.controls[controlName], {
            touched: true,
            value: event.target.value,
            valid: checkValidity(
              event.target.value, this.state.controls[controlName].validation)
          }
        )
      }
    );
    this.setState({ controls: updatedControls });
  }

  submitHandler = (event) => {
    event.preventDefault();
    this.props.onAuth(
      this.state.controls.email.value,
      this.state.controls.password.value, this.state.isSignup );
  }

  switchAuthModeHandler = () => {
    this.setState(prevState => {
      return {
        isSignup: !prevState.isSignup };
    });
  }

  render () {

    const formElementsArray = [];
    for (let key in this.state.controls) {
      formElementsArray.push({
        id: key,
        config: this.state.controls[key]
      });
    }

    let form = formElementsArray.map(formElement => (
      <Input
        key={formElement.id}
        value={formElement.config.value}
        invalid={!formElement.config.valid}
        shouldValidate={formElement.config.validation}
        touched={formElement.config.touched}
        changed={(event) => this.inputChangedHandler(event, formElement.id)}
        elementType={formElement.config.elementType}
        elementConfig={formElement.config.elementConfig} />));

    if ( this.props.loading ) {
      form = <Spinner />;
    }

    let errorMessage = null;
    if ( this.props.error ) {
      errorMessage = (
        <p>{ this.props.error.message }</p>);
    }

    let authRedirect = null;
    if ( this.props.isAuthenticated ) {
      authRedirect = <Redirect to={this.props.authRedirectPath} />
    }


    return (
      <div className={classes.Auth}>
        { authRedirect }
        { errorMessage }
        <form onSubmit={this.submitHandler}>
          { form }
          <Button btnType="Success">Submit</Button>
        </form>
        <Button
          btnType="Danger"
          clicked={this.switchAuthModeHandler}>Switch to { this.state.isSignup ? 'SIGNIN': 'SIGNUP'}</Button>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    error: state.auth.error,
    loading: state.auth.loading,
    isAuthenticated: state.auth.token !== null,
    buildingBurger: state.burgerBuilder.building,
    authRedirectPath: state.auth.authRedirectPath
  };
};

const mapDispatchToProps = dispatch => {
  return {
    onAuth: (email, password, isSignup) => dispatch(actions.auth(email, password, isSignup)),
    onSetAuthRedirectPath: () => dispatch(actions.setAuthRedirectPath('/'))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Auth);
