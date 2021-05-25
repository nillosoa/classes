
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Route, Switch, withRouter, Redirect } from 'react-router-dom';

import asyncComponent from './hoc/asyncComponent/asyncComponent';
import Layout from './hoc/Layout/Layout';
import BurgerBuilder from './containers/BurgerBuilder/BurgerBuilder';
import * as actions from './store/actions';


const asyncAuth = asyncComponent(() => import('./containers/Auth/Auth'));
const asyncLogout = asyncComponent(() => import('./containers/Auth/Logout/Logout'));

const asyncOrders = asyncComponent(() => import('./containers/Orders/Orders'));
const asyncCheckout = asyncComponent(() => import('./containers/Checkout/Checkout'));

class App extends Component {

  componentDidMount () {
    this.props.onTryAutoSignup();
  }

  render() {

    let routes = (
      <Switch>
        <Route exact path="/auth" component={asyncAuth} />
        <Route exact path="/" component={BurgerBuilder} />
        <Redirect to="/" />
      </Switch>
    );

    if ( this.props.isAuthenticated ) {
      routes = (
        <Switch>
          <Route exact path="/auth" component={asyncAuth} />
          <Route exact path="/logout" component={asyncLogout} />
          <Route path="/checkout" component={asyncCheckout} />
          <Route exact path="/orders" component={asyncOrders} />
          <Route exact path="/" component={BurgerBuilder} />
          <Redirect to="/" />
        </Switch>
      );
    }
    return (
      <div>
        <Layout>
          { routes }
        </Layout>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    isAuthenticated: state.auth.token !== null
  };
};

const mapDispatchToProps = dispatch => {
  return {
    onTryAutoSignup: () => dispatch(actions.authCheckState())
  };
};

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(App));
