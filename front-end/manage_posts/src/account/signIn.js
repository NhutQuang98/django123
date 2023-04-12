import React, { useState } from 'react';
import { METHOD_POST } from '../utils/api/methodAxios';

const SignIn = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    METHOD_POST({
      url: `/getAccount`,
      message: 'sign-in',
      param:
      {
        username: username,
        password: password
      }
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <table>
        <tr>
          <th>
            <h2>Sign-In</h2>
          </th>
        </tr>
        <tr>
          <td>
            <input
              type="text"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              placeholder='username enter'
            />
          </td>
        </tr>
        <tr>
          <td>
            <input
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder='password enter'
            />
          </td>
        </tr>
        <tr style={{ textAlign: 'right' }}>
          <button type="submit">Sign-in</button>
        </tr>
      </table>
    </form>
  );
};

export default SignIn;
