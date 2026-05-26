export const jdkColors: Record<string, string> = {
  JDK6: '#ead1dc',
  JDK7: '#d0e0e3',
  JDK8: '#d0e0e3',
  JDK9: '#007bff',
  JDK10: '#b60205',
  JDK11: '#28a745',
  JDK12: '#b6a842',
  JDK13: '#e200db',
  JDK14: '#ff990f',
  JDK15: '#0a9ca2',
  JDK16: '#6600cc',
  JDK17: '#a64d79',
  JDK18: '#454a8e',
  JDK19: '#e43333',
  JDK20: '#083d1c',
  JDK21: '#4acaec',
  JDK22: '#710070',
  JDK23: '#854800',
  JDK24: '#312e81',
  JDK25: '#059669',
  'OLD JDK': '#e3ead1'
}

export function getJdkConfig(label: string) {
  const bg = jdkColors[label] || '#333'
  let text = '#fff'
  let border = bg

  // Special cases for light backgrounds (JDK6, 7, 8, OLD JDK)
  if (['JDK6', 'JDK7', 'JDK8', 'OLD JDK'].includes(label)) {
    text = '#0e2a47'
    border = '#007bff' // Consistent blue border for comparisons as seen in slides
  }
  
  if (label === 'OLD JDK') {
    border = '#a0a88a'
  }

  return { bg, text, border }
}
