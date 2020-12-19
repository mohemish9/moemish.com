//
//  QuestionBank.swift
//  MoodMusic
//
//  Created by Omari Matthews on 10/28/19.
//  Copyright © 2019 Vibe. All rights reserved.
//

import Foundation

class QuestionBank {
    
    // holds the list of survey questions
    var list = [Question]()
    
    // initializes all of the questions listed
    init() {
        list.append(Question(text: "Where are you?",
                             options: ["Public Setting", "Living Room", "Car", "Bedroom", "Office","Outdoors"]))
        list.append(Question(text: "How many people are there?",
                             options: ["1", "2-4", "5-10", ">10"]))
        list.append(Question(text: "How loud do you want it to be?",
        options: ["Calm", "Loud", "Party"]))
        
        list.append(Question(text: "How formal do you want it to be?",
        options: ["Formal", "Casual", "Not Formal"]))
        
    }
    
}
