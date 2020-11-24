import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { withAuth } from '@okta/okta-react';
import "./Home.css";
import Card from "./Card";
import back from './back.jpg'

export default withAuth(
  class Home extends Component {
    state = { authenticated: null };

    checkAuthentication = async () => {
      const authenticated = await this.props.auth.isAuthenticated();
      if (authenticated !== this.state.authenticated) {
        this.setState({ authenticated });
      }
    };

    async componentDidMount() {
      this.checkAuthentication();
    }

    async componentDidUpdate() {
      this.checkAuthentication();
    }

    login = async () => {
      this.props.auth.login('/');
    };

    logout = async () => {
      this.props.auth.logout('/');
    };

    render() {
      if (this.state.authenticated === null) return null;

      const mainContent = this.state.authenticated ? (
        <div>
          <h1 className="display-4" >\n</h1>
          <div className="container1" >
      <div className="row">
        <Card
          title="Medical Insurance Plans"
          images="../images/batman.png"
        />
        <Card
          title="Medicine Recommender"
          images="../images/blackpanter.png"
        />
        <Card
          title="Doctor's Consultation"
          images="../images/arthur.png"
        />
        <Card
          title="Spendings Tracker"
          images="../images/kashima.png"
        />
        <Card
          title="Allergens Alert"
          images="../images/allergy.png"
        />
        <Card
          title="Healthcare Devices"
          images="../images/devices.png"
        />
      </div>
    </div>
          <button className="btn"  onClick={this.logout}>
            Logout
          </button>
        </div>
      ) : (
        <div>
          <h1 className="display-4" >Healthcare Portal</h1>
          <p className="lead">
            If you are a Registered member, please get your credentials by Contacting our Executive.
          </p>
          <button className="btn btn-dark btn-lg" onClick={this.login}>
            Login
          </button>
        </div>
      );

      return (
        <div className="jumbotron">
          <p></p>
          
          {mainContent}
        </div>
      );
    }
  }
);
