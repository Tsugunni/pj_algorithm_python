import React from 'react';
import { ScrollView, StyleSheet } from 'react-native';
import { ExpoLinksView } from '@expo/samples';
import SyntaxHighlighter from 'react-native-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/styles/hljs';

// export default function LinksScreen() {
//   const codeString = '(num) => num + 1';
//   return (
//     <SyntaxHighlighter
//       language='javascript'
//       style={docco}
//       highlighter={"prism" || "hljs"}
//     >
//       {codeString}
//     </SyntaxHighlighter>
//   );
// }


const LinksScreen = () => {
  const codeString = 'ddd';
  return (
    <SyntaxHighlighter language="python" style={docco}>
      {codeString}
    </SyntaxHighlighter>
  )
}
export default LinksScreen;

LinksScreen.navigationOptions = {
  title: '履歴',
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 15,
    backgroundColor: '#fff',
  },
});
