import React from 'react';
import uuid from 'uuid';
import "@fortawesome/fontawesome-free/css/all.min.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import TodoInput from './components/TodoInput';
import TodoList from './components/TodoList';

// showing vs-code github setup
/////
class App extends React.Component {
  render() {
    return (
      <div>
        <div className="container">
          <div className="row">
            <TodoList />
            <TodoInput />

          </div>
        </div>
      </div>
    )
  }
}

export default App;
