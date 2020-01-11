import { AppLoading } from 'expo';
import { Asset } from 'expo-asset';
import * as Font from 'expo-font';
import React, { useState } from 'react';
import { Platform, StatusBar, StyleSheet, View } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

import { withAuthenticator } from 'aws-amplify-react-native';

import AppNavigator from './navigation/AppNavigator';
import awsconfig from './aws-exports';
import Amplify, { I18n } from 'aws-amplify';


Amplify.configure(awsconfig);

function App(props) {
  const [isLoadingComplete, setLoadingComplete] = useState(false);

  if (!isLoadingComplete && !props.skipLoadingScreen) {
    return (
      <AppLoading
        startAsync={loadResourcesAsync}
        onError={handleLoadingError}
        onFinish={() => handleFinishLoading(setLoadingComplete)}
      />
    );
  } else {
    return (
      <View style={styles.container}>
        {Platform.OS === 'ios' && <StatusBar barStyle="default" />}
        <AppNavigator />
      </View>
    );
  }
}

export default withAuthenticator(App, {
  signUpConfig: {
    hiddenDefaults: ['phone_number']
  }
});



async function loadResourcesAsync() {
  await Promise.all([
    Asset.loadAsync([
      require('./assets/images/robot-dev.png'),
      require('./assets/images/robot-prod.png'),
    ]),
    Font.loadAsync({
      // This is the font that we are using for our tab bar
      ...Ionicons.font,
      // We include SpaceMono because we use it in HomeScreen.js. Feel free to
      // remove this if you are not using it in your app
      'space-mono': require('./assets/fonts/SpaceMono-Regular.ttf'),
    }),
  ]);
}

function handleLoadingError(error) {
  // In this case, you might want to report the error to your error reporting
  // service, for example Sentry
  console.warn(error);
}

function handleFinishLoading(setLoadingComplete) {
  setLoadingComplete(true);
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});

const dict = {
  'ja': {
    'Back to Sign In': 'サインイン画面に戻る',
    'Confirm': '確認',
    'Confirm Sign Up': 'サインアップの確認',
    'Confirmation Code': '確認コード',
    'Create Account': '新規登録',
    'Create a new account': 'アカウントの新規登録',
    'Create account': '新規登録',
    'Email': 'メールアドレス',
    'Enter your code': '確認コードを入力してください',
    'Enter your password': 'パスワードを入力してください',
    'Enter your username': 'Enter your email',
    'Forget your password? ': 'パスワードをお忘れの方 ',
    'Have an account? ': 'アカウント登録済みの方 ',
    'Hello': 'こんにちは ',
    'Incorrect username or password': 'ユーザー名またはパスワードが異なります',
    'Lost your code? ': 'コードを紛失した方 ',
    'No account? ': 'アカウント未登録の方 ',
    'Password': 'パスワード',
    'New Password': '新しいパスワード',
    'Submit': '送信する',
    'Invalid verification code provided, please try again.': '検証コードが間違っています 再度試して下さい',
    'Phone Number': '電話番号',
    'Resend Code': '確認コードの再送',
    'Reset password': 'パスワードのリセット',
    'Reset your password': 'パスワードのリセット',
    'Send Code': 'メールに確認コードを送る',
    'Sign In': 'サインイン',
    'Sign Out': 'サインアウト',
    'Sign in': 'サインイン',
    'Code': 'メールの検証コード',
    'Sign in to your account': 'サインイン',
    'User does not exist': 'ユーザーが存在しません',
    'Username': 'メールアドレスを入力して下さい',
    'Username cannot be empty': 'メールアドレスは必須入力です',
    'Username/client id combination not found.': '見つかりません 登録したメールアドレスを入力して下さい',
    'Attempt limit exceeded, please try after some time.': '時間を置いて、再度入力を試して下さい',
    'Your password reset code is': 'エバーフォンの確認コードは'
  }
};

I18n.putVocabularies(dict);
I18n.setLanguage('ja');