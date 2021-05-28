store = {}
store['timestamp']=1622152621
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=15']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=15
store['worker_id']=15
store['num_workers']=40
store['config']={'seed': 1250, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.636814594268799})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6288998126983643})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.4489307403564453})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.803103446960449})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.783226490020752})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.584817886352539})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.170226097106934})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 4.165799140930176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.069317817687988})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6023, 'crossentropy': 3.803246484375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 59392], ['ood', 49889], ['ood', 43312], ['ood', 18502], ['ood', 51363]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6033138243206615, 2.9172040026862156, 3.800103362100378, 4.218251454795817, 4.430247287090082]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.536238670349121})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.68186616897583})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.0046911239624023})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.5267081260681152})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.309422492980957})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.282508373260498})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.442749261856079})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.777986526489258})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.295879364013672})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.4513540267944336})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.520744800567627})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.292611122131348})
store['active_learning_steps'][1]['training']['best_epoch']=9
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6311, 'crossentropy': 3.36444921875}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 11675], ['ood', 55282], ['ood', 56510], ['ood', 30299], ['ood', 20137]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5270133032770183, 2.7548193712307163, 3.657586412837941, 4.140182954115534, 4.3983518021790555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.3421926498413086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.381657600402832})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.342787504196167})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.910393238067627})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5983, 'crossentropy': 2.339676953125}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 28173], ['ood', 10620], ['ood', 47260], ['ood', 39627], ['id', 24014]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.3059034698025418, 2.3099936789263618, 3.112755916251512, 3.6971722511149085, 4.060529060706709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.090289831161499})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.8526453971862793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0948405265808105})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.348153591156006})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5482566356658936})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1354355812072754})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.324932813644409})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5558323860168457})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.8061718940734863})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.7793431282043457})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5768606662750244})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.538041591644287})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.586033821105957})
store['active_learning_steps'][3]['training']['best_epoch']=10
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6017, 'crossentropy': 4.063205078125}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 21935], ['ood', 11455], ['ood', 43823], ['ood', 27113], ['ood', 17728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6742249997035277, 2.9848236349659314, 3.853874350091699, 4.28545984464002, 4.47612158049067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.403961420059204})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.183835983276367})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.5390655994415283})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.578960657119751})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.675640106201172})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.8966667652130127})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.878142833709717})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.9180710315704346})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5958, 'crossentropy': 3.670078515625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 48833], ['ood', 38557], ['ood', 12197], ['ood', 47260], ['id', 907]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.6235691839010689, 2.8294961150500932, 3.638495937870543, 4.1563384061773, 4.392876307978209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.121835231781006})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.620917320251465})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6690380573272705})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8546504974365234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.181973457336426})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1339128017425537})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.7287631034851074})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.300457715988159})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3442933559417725})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6138, 'crossentropy': 3.38174140625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 1194], ['ood', 17876], ['ood', 27393], ['ood', 20023], ['ood', 22661]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.619146847606582, 2.8495378149282553, 3.7099687824865413, 4.184262828144307, 4.416284530809246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1202011108398438})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.59578275680542})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2011842727661133})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.046830654144287})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6292, 'crossentropy': 2.1220134765625}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 37594], ['ood', 12679], ['ood', 26184], ['ood', 32473], ['ood', 23486]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4400032604266313, 2.488180842269575, 3.308851668929406, 3.8614336588393225, 4.188039801992256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.095001697540283})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.760634183883667})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.0823442935943604})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.315747022628784})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2496752738952637})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1716485023498535})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.386019706726074})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.811816453933716})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6223, 'crossentropy': 3.3340953125}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 33976], ['ood', 39153], ['ood', 5806], ['ood', 16911], ['ood', 20093]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4290417550551746, 2.6760393819480224, 3.5702714561385642, 4.074041610796646, 4.346486780885673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.966820240020752})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.780449151992798})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.853057622909546})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.6865928173065186})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.201557159423828})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.296846866607666})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.3523874282836914})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.551605224609375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5058274269104004})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6135, 'crossentropy': 3.413448046875}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 49580], ['ood', 55037], ['ood', 22563], ['ood', 37028], ['ood', 36157]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6343487409554185, 2.961868464025109, 3.846872119218947, 4.291550621555625, 4.471440132399566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.9645190238952637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.3332228660583496})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.845978260040283})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.912036657333374})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.815314292907715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.569042205810547})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0658180713653564})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1741700172424316})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.623703956604004})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2249298095703125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.63284969329834})
store['active_learning_steps'][9]['training']['best_epoch']=8
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6254, 'crossentropy': 3.35949140625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 34331], ['ood', 55970], ['ood', 39427], ['ood', 27131], ['ood', 56553]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5617968836522123, 2.8459030882301617, 3.7902238757552187, 4.259865919765712, 4.460572224170585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.0423712730407715})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.5062685012817383})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6715240478515625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.928187370300293})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8631813526153564})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8398189544677734})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.416651725769043})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6304, 'crossentropy': 3.059288671875}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 12595], ['ood', 54149], ['ood', 36553], ['ood', 11166], ['ood', 42085]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.652530346878835, 2.933756475643704, 3.8038367765309644, 4.2496154769618215, 4.449704483723096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.972116470336914})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.417875289916992})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9293339252471924})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0595505237579346})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9638867378234863})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.34436297416687})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.917116165161133})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6269, 'crossentropy': 3.2104025390625}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 222], ['ood', 17719], ['ood', 10975], ['ood', 22753], ['ood', 28391]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5198306363827336, 2.836127246041076, 3.694793847680087, 4.167140012798617, 4.390789356086714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.039210319519043})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.640822410583496})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.612504482269287})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0839223861694336})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.969909191131592})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2679824829101562})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6234, 'crossentropy': 2.7545142578125}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 13904], ['ood', 13543], ['ood', 13128], ['id', 34620], ['ood', 21055]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.4558196917936006, 2.6719850664715326, 3.4843460103822306, 4.006490527062748, 4.304495022371022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8704464435577393})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.60884952545166})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.966747283935547})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9941463470458984})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8282742500305176})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9013147354125977})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.042280673980713})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6166, 'crossentropy': 3.1657365234375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 24172], ['ood', 21886], ['ood', 48668], ['ood', 57987], ['ood', 59453]], 'labels': [4, -1, -1, -1, -1], 'scores': [1.3968655734928581, 2.654897423157073, 3.5916438378695386, 4.092850068138937, 4.369032356613367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.0303378105163574})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.7692477703094482})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.89105224609375})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1843020915985107})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0938172340393066})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1959736347198486})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.4390416145324707})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.489428997039795})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6084, 'crossentropy': 3.283194140625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 45686], ['ood', 24176], ['ood', 45161], ['ood', 10350], ['ood', 5889]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6073328907214381, 2.9196653765444456, 3.797346713922427, 4.236852497429739, 4.455133165442404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.878363013267517})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.320380687713623})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6178579330444336})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.8753037452697754})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6213, 'crossentropy': 1.9082345703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 19373], ['ood', 52708], ['ood', 36553], ['ood', 27431], ['ood', 23453]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3637850611217237, 2.429958712643008, 3.239552701804371, 3.774761981685037, 4.103778464828489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.1876673698425293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.998886823654175})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.236231803894043})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.4439024925231934})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5158286094665527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.7838048934936523})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.827735185623169})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 4.487479209899902})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5874, 'crossentropy': 3.65873984375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 28493], ['ood', 31497], ['ood', 18547], ['id', 27147], ['ood', 7633]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.6053643030154325, 2.8156693739928347, 3.644935952381582, 4.121864496633291, 4.375701253920347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8959945440292358})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.097933769226074})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.279715061187744})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.70064377784729})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5893828868865967})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6291, 'crossentropy': 2.3570548828125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 10511], ['ood', 43683], ['ood', 36283], ['ood', 42511], ['ood', 23896]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4316878629584466, 2.527563691659933, 3.369745345295552, 3.8775848921608596, 4.195841046462276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.0075252056121826})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.487246036529541})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.557283878326416})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.834228038787842})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1470277309417725})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6178, 'crossentropy': 2.4800990234375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 14073], ['ood', 43636], ['ood', 44377], ['ood', 6917], ['ood', 11111]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3007004471646484, 2.3737585226115647, 3.2031856866544475, 3.778415680547205, 4.1264637329101825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.871657133102417})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.456155776977539})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.6040091514587402})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.730372905731201})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7225232124328613})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8995308876037598})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9313626289367676})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9789299964904785})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2758500576019287})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.406930685043335})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6213, 'crossentropy': 3.0475470703125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 21452], ['ood', 13242], ['ood', 58832], ['ood', 5854], ['ood', 32507]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.437530580415275, 2.6591265706581386, 3.5967900115642717, 4.094632459936264, 4.37433418468426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.826889157295227})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.3185300827026367})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.477569341659546})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.894761562347412})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.9342007637023926})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6245, 'crossentropy': 2.3354353515625}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 25180], ['ood', 5013], ['ood', 10630], ['ood', 9880], ['ood', 17140]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4052286055470264, 2.5573699550602504, 3.3995928184120654, 3.938725438890474, 4.261927031861333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6504501104354858})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.212008476257324})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.431987762451172})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4182379245758057})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8114993572235107})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6683871746063232})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.677206039428711})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8909544944763184})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1715967655181885})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6364, 'crossentropy': 2.841721484375}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 40126], ['ood', 11428], ['ood', 20415], ['ood', 8582], ['ood', 26405]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5022172033167283, 2.722305635181603, 3.6369608974998746, 4.169416420210682, 4.42132234250846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.033323287963867})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.400968551635742})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.874785900115967})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0762176513671875})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.110483169555664})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.113068103790283})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.608, 'crossentropy': 3.096159375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 38954], ['ood', 21992], ['ood', 27293], ['ood', 3677], ['ood', 14823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3894149492726473, 2.543506239017105, 3.3824686764524783, 3.9276755620401147, 4.240934156762802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8481481075286865})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.240671157836914})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.583514451980591})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8013129234313965})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.7434778213500977})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6884031295776367})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.038992404937744})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.7600531578063965})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8214151859283447})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.164210557937622})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 2.96367890625}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 38812], ['ood', 22091], ['ood', 33669], ['ood', 44466], ['ood', 23138]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.602066537435502, 2.8572133946164513, 3.772603898887077, 4.264740965346602, 4.469730344822208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9169858694076538})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.402553081512451})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.599093437194824})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9560437202453613})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.893479347229004})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0839271545410156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.5671863555908203})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6074, 'crossentropy': 3.23485546875}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 3506], ['ood', 21738], ['ood', 52464], ['ood', 32494], ['ood', 16309]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.483929163245686, 2.7205806950949705, 3.6001074964633792, 4.1091721290184084, 4.371585990149426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.121840000152588})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.668191432952881})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.815439462661743})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0318760871887207})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.201934576034546})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4432992935180664})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6153, 'crossentropy': 2.7876701171875}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 2481], ['ood', 38960], ['ood', 33007], ['ood', 27195], ['ood', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3535760767557612, 2.4739854663466705, 3.323686565676187, 3.8627793238253156, 4.197702081171284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.018836498260498})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.4680635929107666})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.540447235107422})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.773780584335327})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.199151039123535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.525428056716919})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6182, 'crossentropy': 2.64117734375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 3574], ['ood', 14103], ['ood', 34708], ['ood', 32451], ['ood', 51415]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.457070163239623, 2.6570813324681435, 3.4911580227230097, 4.0141234884468915, 4.3022712413437585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.9644367694854736})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.824364185333252})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.729855537414551})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.719122886657715})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.792571544647217})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.8747506141662598})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6054, 'crossentropy': 2.8995111328125}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 49251], ['ood', 25848], ['ood', 28391], ['ood', 59441], ['ood', 17048]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5562233665884944, 2.8358957639648406, 3.697636069379424, 4.18010355065762, 4.409684753540873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9015846252441406})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4621076583862305})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.54150128364563})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.041417121887207})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6135, 'crossentropy': 2.0681771484375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 14691], ['ood', 37794], ['ood', 21134], ['ood', 54681], ['ood', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3945980063153893, 2.543495330080317, 3.3202333267281166, 3.829684583351594, 4.1494677015003365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.9898710250854492})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.7151806354522705})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9835500717163086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.960237979888916})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.253718852996826})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4025349617004395})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.5988, 'crossentropy': 2.999744921875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 4737], ['ood', 59333], ['ood', 18598], ['ood', 21487], ['ood', 50835]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4193589478755775, 2.5794447941611613, 3.386303052327701, 3.903593436469432, 4.221399581639956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.7648805379867554})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.407954692840576})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.580657958984375})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.160163402557373})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.1955814361572266})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.4633102416992188})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6077, 'crossentropy': 2.777564453125}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 53280], ['ood', 25311], ['ood', 36715], ['id', 1254], ['ood', 27498]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.4356921498563977, 2.655838092393056, 3.4570881230607924, 3.9739308153201574, 4.276665070802288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8548529148101807})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.2071003913879395})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5632619857788086})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8538341522216797})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9394400119781494})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 2.3228548828125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 46907], ['ood', 17428], ['ood', 36553], ['ood', 35930], ['ood', 46597]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.45614215900708, 2.7025068287705913, 3.583725649677911, 4.095893951172613, 4.373885834557493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.8343055248260498})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.3480193614959717})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6789369583129883})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.869187831878662})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.879591941833496})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.883340358734131})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.2304346561431885})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.99916934967041})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.850949764251709})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.266390800476074})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6401, 'crossentropy': 3.335354296875}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 25180], ['ood', 10253], ['ood', 26358], ['ood', 28324], ['ood', 27077]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6877510935049278, 2.999575962007496, 3.7966372141020805, 4.253173716262541, 4.462355683500576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9775440692901611})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.231358051300049})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5841805934906006})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.658111572265625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.819995403289795})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.206916332244873})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6219, 'crossentropy': 2.6924943359375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 42676], ['ood', 24968], ['ood', 48437], ['ood', 15973], ['ood', 12053]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4706650614797174, 2.681428619700834, 3.5772621762136314, 4.079617418751261, 4.352829520218187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8564565181732178})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3815038204193115})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.729691982269287})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.88816499710083})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.5997, 'crossentropy': 2.0202978515625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 4730], ['ood', 58560], ['ood', 45031], ['ood', 47260], ['ood', 14111]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3014430001813446, 2.3748277677964342, 3.156184295931393, 3.689016008759097, 4.056615113358355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.882349967956543})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4681997299194336})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.600979804992676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1090035438537598})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1526131629943848})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.148721218109131})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6275, 'crossentropy': 2.7150580078125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 24076], ['ood', 28558], ['ood', 54425], ['ood', 48284], ['ood', 48794]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5741201848242876, 2.738711886243193, 3.6122773045830083, 4.11872706187869, 4.360866340893491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7782046794891357})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1275594234466553})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4474596977233887})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.780459403991699})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.614, 'crossentropy': 1.9071234375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 36080], ['ood', 21668], ['ood', 18501], ['ood', 5013], ['ood', 49616]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3572779258408878, 2.4318414771984704, 3.2341784782107688, 3.771814311516433, 4.106580046031688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.760420322418213})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.2038733959198})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.4404172897338867})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.39571213722229})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.56447696685791})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.660289764404297})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.622159481048584})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6366, 'crossentropy': 2.5475396484375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 36970], ['ood', 37386], ['ood', 59395], ['ood', 23790], ['ood', 35030]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.522015085330148, 2.8345555105290163, 3.6834193790094396, 4.166125526088238, 4.3824563788707565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.003410816192627})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.581456184387207})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.7731528282165527})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.695420980453491})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9952104091644287})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6281, 'crossentropy': 2.58067109375}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 42583], ['ood', 35662], ['ood', 37425], ['ood', 46456], ['ood', 38326]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5260470681976246, 2.7187957165453627, 3.527880389127919, 4.015349649370011, 4.289515148090883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.844313383102417})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.3753252029418945})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.7402806282043457})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.739898204803467})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8129525184631348})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.894773006439209})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.775670051574707})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.938723087310791})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.863107919692993})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6233, 'crossentropy': 3.11526015625}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 56811], ['ood', 19677], ['ood', 5013], ['ood', 59367], ['ood', 37777]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6524369466531508, 2.922682169587621, 3.778676318905852, 4.278523909951209, 4.4734593306675885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.0462584495544434})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.3160648345947266})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.7600345611572266})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.938509464263916})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.092280149459839})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6187, 'crossentropy': 2.357916796875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 29380], ['ood', 1225], ['id', 23510], ['ood', 50026], ['ood', 25683]], 'labels': [-1, -1, 1, -1, -1], 'scores': [1.3612150676641632, 2.4727870413531083, 3.3426769531729903, 3.8761991067605486, 4.213880808892528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.6707193851470947})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4483232498168945})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4325051307678223})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.720613718032837})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.993438243865967})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6352, 'crossentropy': 2.483662109375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 4757], ['ood', 21803], ['ood', 56335], ['ood', 6857], ['ood', 29180]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5180131707564266, 2.605167843145318, 3.4090389327919475, 3.9391811013435056, 4.2346701163941995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.8629966974258423})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1206207275390625})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5282115936279297})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6447839736938477})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7372710704803467})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9233288764953613})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8359718322753906})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6308, 'crossentropy': 2.751873046875}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 27293], ['ood', 48029], ['ood', 40224], ['ood', 48337], ['ood', 59744]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.53111856844792, 2.7755484479734767, 3.735823544825215, 4.202411700843712, 4.43621973641103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.9616127014160156})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.499906063079834})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7329788208007812})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.848757266998291})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1790153980255127})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2815775871276855})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.6756954193115234})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.076422265625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 20050], ['ood', 35930], ['ood', 19611], ['ood', 57349], ['ood', 2360]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4796137682043535, 2.763088435551386, 3.665691528842025, 4.18234123828859, 4.415550040101197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.7696640491485596})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.090759515762329})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3076517581939697})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5544180870056152})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.649690628051758})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6428, 'crossentropy': 2.161646875}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 25180], ['ood', 30885], ['ood', 50930], ['ood', 56888], ['ood', 19952]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5260123619347206, 2.717108947560713, 3.5157517624646317, 4.008378754320812, 4.278518466734566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.016068935394287})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2367935180664062})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.460768222808838})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.594524621963501})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.686674118041992})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.67330265045166})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.921332597732544})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.878431797027588})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8468499183654785})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6216, 'crossentropy': 2.9728873046875}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 25341], ['ood', 40394], ['ood', 42080], ['ood', 39128], ['ood', 46457]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6786307275261754, 2.964149555167041, 3.8381199884659187, 4.296721038570853, 4.481273772563775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7779957056045532})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.418753147125244})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3082425594329834})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.642454147338867})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7814126014709473})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.649341106414795})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6282, 'crossentropy': 2.488914453125}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 42676], ['ood', 42605], ['ood', 19573], ['ood', 2126], ['ood', 21279]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5326169471991304, 2.7860920458107112, 3.6020096202890857, 4.113928012387936, 4.36885785612389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8333065509796143})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.299208402633667})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4947011470794678})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.530437469482422})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9044599533081055})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.0247883796691895})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6173, 'crossentropy': 2.6753392578125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 41468], ['ood', 53280], ['ood', 14600], ['ood', 28391], ['ood', 36879]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5301670801607328, 2.751736061419008, 3.6275095961148835, 4.110626031693015, 4.371145771844018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9880480766296387})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.3873212337493896})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5061817169189453})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6759347915649414})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9286346435546875})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.7341933250427246})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.9342970848083496})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3119144439697266})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.149068832397461})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6372, 'crossentropy': 2.958046875}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 222], ['ood', 48678], ['ood', 20897], ['ood', 21358], ['ood', 47592]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5330598450468162, 2.7826070768062308, 3.6438010877025535, 4.164075812586711, 4.405809398744446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8533260822296143})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.559800148010254})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.414236068725586})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6560912132263184})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.719993829727173})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.525318145751953})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6133, 'crossentropy': 2.592298828125}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 222], ['ood', 15867], ['ood', 44952], ['ood', 30220], ['ood', 59731]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.458718509945806, 2.674843916624661, 3.515636290653217, 4.042239820080892, 4.336955229702991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.0165371894836426})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1942100524902344})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5894060134887695})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0577244758605957})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8706626892089844})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9049105644226074})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.989170789718628})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.117459774017334})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6284, 'crossentropy': 2.9558509765625}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 11465], ['ood', 31046], ['ood', 4414], ['ood', 32160], ['ood', 5975]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.505430057318748, 2.6770351359565616, 3.565609012930458, 4.085555822936306, 4.355426870923497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8591666221618652})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.5735721588134766})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.962332248687744})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.03971004486084})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.883018970489502})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.8514063358306885})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6201, 'crossentropy': 2.8427880859375}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 46194], ['ood', 14619], ['ood', 24758], ['ood', 48337], ['ood', 14807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5713105484143013, 2.6912797901119543, 3.553509963892915, 4.067353257280597, 4.340830053308533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9126431941986084})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.38620662689209})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6262824535369873})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6540756225585938})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.048518657684326})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.889237403869629})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.175271511077881})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9635157585144043})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2094247341156006})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.626, 'crossentropy': 3.1312640625}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 50089], ['ood', 1275], ['id', 17871], ['ood', 21279], ['ood', 42832]], 'labels': [-1, -1, 0, -1, -1], 'scores': [1.665728553315018, 3.0005688018547687, 3.8479875220445283, 4.295921909262732, 4.487576041713065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7842049598693848})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8624005317687988})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.259486675262451})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.1716299057006836})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4553232192993164})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.790339946746826})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6616153717041016})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6521, 'crossentropy': 2.33299375}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 46148], ['ood', 45725], ['ood', 32895], ['ood', 20357], ['ood', 22121]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4635496227265976, 2.7253112335609706, 3.613127479221605, 4.132153080307878, 4.394331272461451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9456567764282227})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.4367024898529053})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4983015060424805})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6814708709716797})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6394, 'crossentropy': 1.8530658203125}
