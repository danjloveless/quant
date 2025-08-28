import SwiftUI

// QUANTFIN App Styles
struct QUANTFINStyles {
    static let primaryColor = Color(red: 50/255, green: 130/255, blue: 184/255)
    static let backgroundColor = Color.white
    static let textColor = Color(red: 38/255, green: 39/255, blue: 48/255)
    
    static let launchScreen = AnyView(
        ZStack {
            backgroundColor
                .edgesIgnoringSafeArea(.all)
            
            VStack(spacing: 20) {
                Image(systemName: "chart.line.uptrend.xyaxis")
                    .resizable()
                    .frame(width: 80, height: 80)
                    .foregroundColor(primaryColor)
                
                Text("QUANTFIN")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .foregroundColor(primaryColor)
                
                Text("Society Research")
                    .font(.subheadline)
                    .foregroundColor(textColor)
            }
        }
    )
}