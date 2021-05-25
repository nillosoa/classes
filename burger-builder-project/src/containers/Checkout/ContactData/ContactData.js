
import React, { Component } from 'react';
import { connect } from 'react-redux';

import classes from './ContactData.css';
import axios from '../../../axios-orders';
import Spinner from '../../../components/UI/Spinner/Spinner';
import Button from '../../../components/UI/Button/Button';
import Input from '../../../components/UI/Input/Input';
import withErrorHandler from '../../../hoc/withErrorHandler/withErrorHandler';
import * as actions from '../../../store/actions';
import { updateObject, checkValidity } from '../../../shared/utility';


class ContactData extends Component {
  state = {
    orderForm: {
      name: {
        value: '',
        valid: false,
        validation: {
          required: true
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'text',
          placeholder: 'Your Name'
        }
      },
      email: {
        value: '',
        valid: false,
        validation: {
          required: true
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'email',
          placeholder: 'Your Email'
        }
      },
      street: {
        value: '',
        valid: false,
        validation: {
          required: true
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'text',
          placeholder: 'Your Street Address'
        }
      },
      zipCode: {
        value: '',
        valid: false,
        validation: {
          required: true,
          minLength: 5,
          maxLength: 5
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'text',
          placeholder: 'Zipcode'
        }
      },
      country: {
        value: '',
        valid: false,
        validation: {
          required: true
        },
        touched: false,
        elementType: 'input',
        elementConfig: {
          type: 'text',
          placeholder: 'Country'
        }
      },
      deliveryMethod: {
        value: 'fastest',
        elementType: 'select',
        elementConfig: {
          options: [
            {value: 'fastest', displayValue: 'Fastest'},
            {value: 'cheapest', displayValue: 'Cheapest'}
          ]
        }
      }
    },
    formIsValid: false
  }

  orderHandler = (event) => {
    event.preventDefault();

    const formData = {};
    for (let formElementIdentifier in this.state.orderForm) {
      formData[formElementIdentifier] = this.state.orderForm[formElementIdentifier].value;
    }
    const order = {
      orderData: formData,
      price: this.props.price,
      ingredients: this.props.ings,
      userId: this.props.userId
    };

    this.props.onOrderBurger(order, this.props.token);

  }

  inputChangedHandler = (event, inputIdentifier) => {
    const updatedFormElement = updateObject(
      this.state.orderForm[inputIdentifier], {
        value: event.target.value,
        valid: checkValidity(
          event.target.value,
          this.state.orderForm[inputIdentifier].validation),
        touched: true
      });

    const updatedOrderForm = updateObject(
      this.state.orderForm, {
        [inputIdentifier]: updatedFormElement
      });

    let formIsValid = true;
    for (let inputIdentifier in updatedOrderForm) {
      const valid = updatedOrderForm[inputIdentifier].valid;
      formIsValid = (valid || (valid === undefined || valid === null)) && formIsValid;
    } 

    this.setState({
        orderForm: updatedOrderForm,
        formIsValid:  updatedFormElement.valid && formIsValid
    });
  }

  render () {

    const formElementsArray = [];
    for (let key in this.state.orderForm) {
      formElementsArray.push({
        id: key,
        config: this.state.orderForm[key]
      })
    }

    let form = (
      <form onSubmit={this.orderHandler}>
        {
          formElementsArray.map(formElement => (
            <Input
              key={formElement.id}
              value={formElement.config.value}
              invalid={!formElement.config.valid}
              shouldValidate={formElement.config.validation}
              touched={formElement.config.touched}
              changed={(event) => this.inputChangedHandler(event, formElement.id)}
              elementType={formElement.config.elementType}
              elementConfig={formElement.config.elementConfig} />
          ))
        }
        <Button btnType="Success" disabled={!this.state.formIsValid}>ORDER</Button>
      </form>
    );

    if ( this.props.loading ) {
      form = <Spinner />;
    }

    return (
      <div className={classes.ContactData}>
        <h4>Enter your Contact Data</h4>
        { form }
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    userId: state.auth.userId,
    ings: state.burgerBuilder.ingredients,
    price: state.burgerBuilder.totalPrice,
    loading: state.order.loading
  };
};

const mapDispatchToProps = dispatch => {
  return {
    onOrderBurger: (orderData, token) => dispatch(actions.purchaseBurger(orderData, token))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(withErrorHandler(ContactData, axios));
