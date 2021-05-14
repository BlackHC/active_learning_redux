store = {}
store['timestamp']=1620992156
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=16']
store['commit']='50fc0561f6557d261400d89a96a1c6ef6418247b'
store['github_url']='50fc0561f6557d261400d89a96a1c6ef6418247b'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=20
store['config']={'seed': 1258, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.18837571144104})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.682811737060547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9211511611938477})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.765324592590332})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6816, 'crossentropy': 1.994144921875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.196800947189331})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1787054538726807})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1686885356903076})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [57276, 56777, 14184, 12955, 35533, 4066, 24190, 35018, 35097, 20491], 'labels': [8, 0, 3, 4, 4, 1, 8, 8, 5, 8], 'scores': [0.7638651728630066, 0.9526365399360657, 0.7528903484344482, 0.5988413095474243, 0.7343253493309021, 0.9766759276390076, 0.6722263693809509, 0.6853373050689697, 0.8929271697998047, 0.7399305105209351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3742189407348633})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.4301958084106445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.81027889251709})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.6743974685668945})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.726, 'crossentropy': 1.9720986328125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1850557327270508})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1300442218780518})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1142159700393677})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [30932, 36861, 42530, 570, 6196, 671, 10307, 5348, 55660, 47987], 'labels': [0, 8, 6, 2, 8, 1, 6, 8, 6, 9], 'scores': [0.6318655610084534, 0.6447831392288208, 0.7804855704307556, 0.7614263296127319, 0.44151973724365234, 0.7303924560546875, 0.8247595429420471, 0.7741833329200745, 0.7148237228393555, 0.6323229074478149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6045341491699219})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5827264785766602})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.7008600234985352})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.9450937509536743})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.110067129135132})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7961, 'crossentropy': 1.3746771484375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8854368925094604})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8079583644866943})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.8197061419487})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.7912507057189941})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [18003, 16993, 4113, 33340, 46946, 8744, 33126, 4901, 39449, 30483], 'labels': [2, 5, 5, 5, 9, 5, 9, 9, -1, 3], 'scores': [0.7133448123931885, 0.5175867080688477, 0.7553057074546814, 0.7153699398040771, 0.761084794998169, 0.6815392971038818, 0.7421155571937561, 0.6649301052093506, 0.3438633680343628, 0.6821386218070984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4151203632354736})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.5261955261230469})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.8963085412979126})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.540677547454834})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7714, 'crossentropy': 1.20958232421875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.9965733289718628})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9384498596191406})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.902241587638855})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [51407, 57307, 25986, 21009, 20441, 15500, 46400, 48215, 1923, 54943], 'labels': [6, 2, 8, 2, 2, 6, 2, 4, 2, 0], 'scores': [0.6255605220794678, 0.5962077379226685, 0.4628269076347351, 0.8116185665130615, 0.6525437831878662, 0.5347152948379517, 0.8003689050674438, 0.5065876841545105, 0.5989556312561035, 0.5868380665779114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1979342699050903})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4929168224334717})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3396291732788086})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.394623875617981})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8214, 'crossentropy': 1.02759189453125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9095286130905151})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8571314215660095})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7959034442901611})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [9380, 1917, 32212, 18098, 55404, 26615, 11269, 1833, 27235, 9830], 'labels': [3, 6, 2, 4, 2, -1, 0, 7, 7, 2], 'scores': [0.5105598568916321, 0.517139196395874, 0.5503950119018555, 0.3906351923942566, 0.5468761920928955, 0.4389532804489136, 0.5275095105171204, 0.5277225375175476, 0.7232714891433716, 0.5466305017471313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9061640501022339})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.024080514907837})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1636550426483154})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0464719533920288})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8272, 'crossentropy': 0.88060322265625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8545538187026978})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7948147058486938})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7623440027236938})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [35784, 1642, 10375, 12188, 16823, 32875, 13191, 11270, 46961, 34115], 'labels': [5, 6, 6, 7, 7, 5, 9, 5, 9, 5], 'scores': [0.480326771736145, 0.5244086384773254, 0.3557157516479492, 0.4899688959121704, 0.43039727210998535, 0.43965375423431396, 0.3480788469314575, 0.3957023620605469, 0.4727506637573242, 0.560931921005249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9061159491539001})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.906615138053894})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0396981239318848})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9866948127746582})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8429, 'crossentropy': 0.8871669921875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8445011377334595})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7577518224716187})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7515126466751099})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [42707, 50433, 58237, 5216, 25111, 27866, 46540, 30041, 12957, 15767], 'labels': [3, 4, 3, 2, 5, 3, 2, -1, 5, 5], 'scores': [0.5703979134559631, 0.479769229888916, 0.6999931931495667, 0.3892934322357178, 0.4394071102142334, 0.4901607632637024, 0.3458380699157715, 0.3308178186416626, 0.7067446708679199, 0.6156123876571655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9276962876319885})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9328846335411072})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8202519416809082})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0084831714630127})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9256138205528259})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9758014678955078})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.698722021484375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6874339580535889})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6250810027122498})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5471932888031006})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5419729948043823})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5237930417060852})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [16749, 11556, 41602, 1299, 43498, 14309, 24482, 1370, 50248, 7050], 'labels': [0, -1, 5, 2, -1, 1, 9, 9, -1, 0], 'scores': [0.6295303106307983, 0.41606152057647705, 0.7722374200820923, 0.6225342452526093, 0.593361496925354, 0.5772081017494202, 0.4469990134239197, 0.6118755340576172, 0.41726934909820557, 0.6819758117198944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8285990953445435})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7845758199691772})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8843780755996704})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8497501611709595})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8535760641098022})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8936, 'crossentropy': 0.680487353515625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7655986547470093})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5961029529571533})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6010724306106567})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5385912656784058})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [8848, 33760, 53083, 42287, 53118, 55496, 19337, 52460, 5164, 33409], 'labels': [6, 3, 3, 5, -1, 9, 3, 7, -1, 5], 'scores': [0.3453388810157776, 0.613783061504364, 0.4014909863471985, 0.41576099395751953, 0.4469132423400879, 0.48805248737335205, 0.3833490014076233, 0.36197298765182495, 0.5338553190231323, 0.4543275833129883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8965988159179688})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7561764717102051})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.779288649559021})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8589245080947876})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9564552307128906})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.65428876953125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7190011739730835})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5911802053451538})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5531816482543945})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5577874183654785})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [11734, 30883, 39267, 40275, 26034, 9677, 43402, 51145, 9100, 23463], 'labels': [8, 3, 3, -1, 5, -1, 5, 9, -1, 9], 'scores': [0.5572584867477417, 0.5277308821678162, 0.44435667991638184, 0.3218719959259033, 0.6738896369934082, 0.30537134408950806, 0.4560321569442749, 0.30845314264297485, 0.40228158235549927, 0.49187082052230835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9564454555511475})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8179436326026917})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9227849841117859})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9998350143432617})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9228389263153076})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8963, 'crossentropy': 0.69011865234375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.795799732208252})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5777055621147156})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.570965051651001})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5608946681022644})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [12497, 47951, 1916, 14749, 8833, 22606, 31014, 16272, 53344, 30188], 'labels': [0, 5, 0, 0, 2, 2, 8, -1, 0, 7], 'scores': [0.7551209926605225, 0.7056559920310974, 0.6752675771713257, 0.5776264071464539, 0.5314779877662659, 0.4033595323562622, 0.5120686292648315, 0.4187607765197754, 0.5490438342094421, 0.6136409044265747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8854210376739502})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7988067269325256})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7692134976387024})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7868996858596802})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8661247491836548})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8030115962028503})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.629466650390625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7626553773880005})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.582809567451477})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5649054050445557})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.48532164096832275})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.48410528898239136})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [4955, 9248, 50391, 5666, 17521, 53043, 28468, 34059, 51775, 20169], 'labels': [2, 2, 9, -1, 3, 8, 4, 6, -1, 4], 'scores': [0.49495625495910645, 0.45617592334747314, 0.5462656617164612, 0.5459895133972168, 0.600284993648529, 0.583422839641571, 0.5260769128799438, 0.4198932647705078, 0.5237303972244263, 0.6354220509529114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7754994630813599})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7075227499008179})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6614981293678284})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6883705854415894})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7411335110664368})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7095628976821899})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.58802763671875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7174220085144043})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5322877764701843})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5477417707443237})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.47257155179977417})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.45108121633529663})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [30095, 41151, 26061, 58469, 17941, 10116, 38518, 36304, 13946, 22083], 'labels': [9, 7, 8, 9, 0, 3, -1, 0, 5, 2], 'scores': [0.3811710476875305, 0.6408053040504456, 0.4130401611328125, 0.5493228137493134, 0.4271300435066223, 0.4991222620010376, 0.3405263423919678, 0.5095921158790588, 0.38800048828125, 0.7098171710968018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8781387805938721})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6595702171325684})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6357511281967163})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6564111113548279})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.66571044921875})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7423173189163208})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9122, 'crossentropy': 0.596341455078125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7715093493461609})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5674519538879395})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5236586332321167})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5165743827819824})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.45286044478416443})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [3094, 50555, 13834, 32152, 12241, 41551, 37275, 47291, 10662, 30927], 'labels': [8, -1, 7, 9, -1, -1, 5, 1, -1, -1], 'scores': [0.5482450723648071, 0.46746140718460083, 0.21823668479919434, 0.5921831130981445, 0.5584444403648376, 0.42032188177108765, 0.6633414030075073, 0.45229417085647583, 0.4218229055404663, 0.48037827014923096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8507825136184692})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6248128414154053})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5618688464164734})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6865585446357727})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6895772218704224})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.750255286693573})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.499640869140625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7242344617843628})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5931110382080078})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5163292288780212})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4951826333999634})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.461242139339447})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [36834, 35931, 17657, 39130, 32510, 43702, 37816, 41347, 49589, 8691], 'labels': [-1, -1, 6, 6, 2, 3, 1, 8, 3, 2], 'scores': [0.37280893325805664, 0.32075440883636475, 0.3414158225059509, 0.5179962515830994, 0.6067641377449036, 0.4529260993003845, 0.44052958488464355, 0.42028045654296875, 0.49189120531082153, 0.5935265421867371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8433700799942017})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6358234882354736})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6262040138244629})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6872954368591309})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6312917470932007})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.712069034576416})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.54577841796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7331314086914062})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5844842195510864})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5258786678314209})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.486595094203949})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4592380225658417})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [20228, 18580, 17590, 19981, 23534, 31225, 30176, 34211, 50135, 7233], 'labels': [9, 8, 4, 8, -1, 9, -1, 9, 6, 9], 'scores': [0.5352404117584229, 0.48867350816726685, 0.5345438718795776, 0.493042528629303, 0.3117082118988037, 0.514905571937561, 0.3393741846084595, 0.4806821346282959, 0.4482080340385437, 0.5020378828048706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8682748079299927})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7469959855079651})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6615797281265259})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6106618642807007})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6581501960754395})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6811103820800781})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7192062139511108})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.53718251953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7534940242767334})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5292246341705322})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.44440436363220215})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4581682085990906})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.43399351835250854})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.42503172159194946})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [30131, 31345, 40237, 16882, 32315, 48347, 39835, 30607, 8867, 2184], 'labels': [3, 3, -1, 7, 1, -1, 7, -1, 8, 2], 'scores': [0.5657904744148254, 0.5515624284744263, 0.5617990493774414, 0.4914756417274475, 0.37765008211135864, 0.3858689069747925, 0.63186115026474, 0.405470609664917, 0.5370849370956421, 0.3560832440853119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8518611192703247})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6819255352020264})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5832076668739319})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6026362776756287})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6216002702713013})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5992200374603271})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.5257708984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7754069566726685})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5208786129951477})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4923632740974426})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.466666579246521})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.44344449043273926})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [47594, 34666, 58258, 15344, 5425, 53736, 46106, 46832, 24434, 13242], 'labels': [3, 7, 7, 0, 1, 9, 7, 7, 7, 3], 'scores': [0.42947930097579956, 0.4899492859840393, 0.505744993686676, 0.30095452070236206, 0.4288414716720581, 0.4964190125465393, 0.4906894564628601, 0.4955753684043884, 0.5015851259231567, 0.554972767829895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8931097984313965})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5561673045158386})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5910021066665649})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5886651277542114})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6187450885772705})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.49140439453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7543106079101562})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5265416502952576})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5399518013000488})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45120692253112793})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [36268, 52644, 15715, 38645, 44381, 13185, 50728, 48038, 38253, 15693], 'labels': [5, 7, 2, 4, 5, 5, 3, 3, 4, -1], 'scores': [0.4394524097442627, 0.3002389073371887, 0.42585980892181396, 0.45727241039276123, 0.4824867844581604, 0.5469182729721069, 0.47573238611221313, 0.44940483570098877, 0.45460379123687744, 0.220625638961792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9380613565444946})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5870447158813477})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6313597559928894})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5585265159606934})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5974082350730896})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6061935424804688})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6073837876319885})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.47579140625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7673841118812561})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5071569085121155})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4430330991744995})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41955286264419556})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3902626633644104})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39284396171569824})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [56168, 47595, 28666, 890, 47680, 35000, 18950, 42799, 17356, 17478], 'labels': [2, 7, 5, -1, 4, -1, 7, 2, -1, 4], 'scores': [0.3786350041627884, 0.3492872714996338, 0.5761831104755402, 0.4694017171859741, 0.5190162062644958, 0.32250404357910156, 0.32559335231781006, 0.5398092865943909, 0.44602417945861816, 0.4047554135322571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9505510330200195})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5076043605804443})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4740957021713257})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5169533491134644})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5635355114936829})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5676910281181335})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.42639677734375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7469495534896851})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5195653438568115})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4894421696662903})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4002094864845276})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3890964388847351})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [7513, 25781, 58642, 42317, 30698, 38397, 12189, 5106, 25757, 20636], 'labels': [-1, -1, 3, 5, 9, 8, -1, 9, -1, 9], 'scores': [0.24089860916137695, 0.21626651287078857, 0.23262393474578857, 0.40885865688323975, 0.434612512588501, 0.4206899404525757, 0.2748497724533081, 0.6040595173835754, 0.4990886449813843, 0.5407673716545105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9608970880508423})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6130985617637634})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4744212031364441})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48204582929611206})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4686494469642639})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49806562066078186})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47087472677230835})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5043662786483765})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.422692138671875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8321725726127625})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4781847298145294})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.415423721075058})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3650680184364319})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34674614667892456})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34170135855674744})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33167701959609985})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [29226, 47322, 20659, 49505, 17083, 44340, 43801, 21147, 8704, 53006], 'labels': [6, 8, 1, 6, 6, -1, -1, -1, 1, 8], 'scores': [0.3072945475578308, 0.5898286998271942, 0.5375056266784668, 0.7489328384399414, 0.41377586126327515, 0.463101863861084, 0.5049446225166321, 0.3127727508544922, 0.6806610822677612, 0.5470370054244995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8423185348510742})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5346145033836365})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48924490809440613})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47185659408569336})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5202505588531494})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5234036445617676})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5280566215515137})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.432189306640625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7429458498954773})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4976511001586914})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43348419666290283})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4245491027832031})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4171063005924225})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40037861466407776})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [14372, 7616, 25477, 42212, 46285, 32747, 6556, 43549, 28786, 53651], 'labels': [-1, -1, 8, -1, 8, 8, -1, -1, -1, -1], 'scores': [0.36775004863739014, 0.34941399097442627, 0.38071775436401367, 0.4344754219055176, 0.4836956858634949, 0.4636662006378174, 0.2787148952484131, 0.42792510986328125, 0.23594844341278076, 0.40982699394226074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8671561479568481})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5900295376777649})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46529948711395264})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4962644577026367})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5118994116783142})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5285905599594116})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9409, 'crossentropy': 0.397828125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8697778582572937})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5639115571975708})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5004937648773193})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43042123317718506})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43576687574386597})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [39605, 2092, 47579, 26048, 45801, 46397, 18879, 17924, 54433, 49664], 'labels': [-1, 3, -1, 3, 3, -1, -1, -1, -1, -1], 'scores': [0.49396538734436035, 0.4983302354812622, 0.1885826587677002, 0.4444822072982788, 0.47573667764663696, 0.27908337116241455, 0.4111135005950928, 0.3962082862854004, 0.40075546503067017, 0.27344679832458496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8572641611099243})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5913879871368408})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4854263961315155})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.459158718585968})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.503275990486145})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46632474660873413})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5394855737686157})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.3539460205078125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8065885305404663})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.48241642117500305})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4256138205528259})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3991939127445221})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38038671016693115})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37699806690216064})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [11216, 33388, 32002, 45491, 37249, 53492, 11298, 50340, 11569, 14204], 'labels': [-1, -1, 6, 5, 5, 4, 2, 3, 5, 5], 'scores': [0.28751492500305176, 0.27633488178253174, 0.3749842047691345, 0.5381190776824951, 0.503865122795105, 0.3434746265411377, 0.4680561125278473, 0.33621862530708313, 0.3552227020263672, 0.6728813648223877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9427465200424194})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5008198022842407})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47017166018486023})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4466179609298706})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.430125892162323})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4293687641620636})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4848063290119171})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5004686117172241})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.538048267364502})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.375286474609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7574697732925415})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46617257595062256})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4166399836540222})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3692930340766907})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3434373736381531})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3434997498989105})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3320310115814209})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32125139236450195})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [134, 52097, 42078, 8432, 54455, 40016, 56514, 30462, 46277, 29952], 'labels': [1, 1, 4, 8, 4, -1, 2, -1, -1, 1], 'scores': [0.5383787751197815, 0.5585361123085022, 0.6154130101203918, 0.5911033749580383, 0.2645828127861023, 0.5267070531845093, 0.6194437146186829, 0.44576960802078247, 0.4641073942184448, 0.5235745310783386]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9166563153266907})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.477847158908844})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48236727714538574})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44822561740875244})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4328562319278717})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45777076482772827})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43620121479034424})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48931461572647095})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9491, 'crossentropy': 0.3598394775390625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7778722047805786})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49187690019607544})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40845435857772827})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3632015585899353})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32668453454971313})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35476216673851013})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3230242133140564})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [37688, 58832, 56346, 32738, 18738, 55677, 1160, 51522, 6466, 28512], 'labels': [9, 3, 7, 7, 9, 3, 4, 3, 2, 5], 'scores': [0.49045059084892273, 0.4378569722175598, 0.4744199514389038, 0.5023356676101685, 0.36791834235191345, 0.3985830545425415, 0.4729689359664917, 0.5154213905334473, 0.4517570734024048, 0.5357210040092468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9513266682624817})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5524578094482422})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4288724660873413})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43451330065727234})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46084269881248474})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44879502058029175})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.3790043212890625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7659932374954224})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49084991216659546})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4665861427783966})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41564592719078064})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3969445824623108})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [5315, 29360, 7146, 16951, 30451, 3941, 20170, 29034, 38656, 148], 'labels': [3, 8, 2, 8, 8, 3, 9, 0, 5, 7], 'scores': [0.4595569968223572, 0.46412742137908936, 0.37120580673217773, 0.4688299894332886, 0.5668591260910034, 0.538906455039978, 0.5089600086212158, 0.3154143691062927, 0.4018673896789551, 0.3360947370529175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0142908096313477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5135579705238342})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4580235481262207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4352567195892334})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4070087671279907})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4018753468990326})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44124895334243774})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4521538019180298})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4288417398929596})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9519, 'crossentropy': 0.357383349609375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7573482394218445})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4673895835876465})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43627578020095825})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37125295400619507})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33557161688804626})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33506569266319275})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33619454503059387})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3191174268722534})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [46272, 31828, 41099, 34097, 50054, 51000, 30282, 53102, 10692, 32453], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, 1, 8], 'scores': [0.3568885326385498, 0.38907766342163086, 0.3591345548629761, 0.42348533868789673, 0.5593822002410889, 0.4235532283782959, 0.30939674377441406, 0.44555187225341797, 0.339219868183136, 0.4798605442047119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9173670411109924})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5104697346687317})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42743903398513794})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4341025650501251})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44164562225341797})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46869462728500366})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.374436962890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7965417504310608})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5016182661056519})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4263148605823517})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3936617374420166})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4283832907676697})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [2682, 40704, 740, 52392, 34785, 9118, 1468, 34542, 29470, 11586], 'labels': [8, 5, 8, 1, 8, 9, 5, 1, -1, 8], 'scores': [0.44272327423095703, 0.4529554843902588, 0.4777052402496338, 0.32163238525390625, 0.5184186100959778, 0.592785120010376, 0.29452088475227356, 0.41629981994628906, 0.32784950733184814, 0.5806973576545715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1155017614364624})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5132499933242798})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43856576085090637})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4386986196041107})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41485726833343506})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4164904057979584})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4195173382759094})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45193105936050415})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.3544762939453125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6492977738380432})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.397596538066864})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3623121976852417})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34013083577156067})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3362414836883545})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3160262107849121})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28624671697616577})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [57524, 54556, 54858, 23350, 51764, 23868, 3762, 24479, 12630, 31200], 'labels': [4, 2, 3, 8, 5, 9, 8, 8, -1, 9], 'scores': [0.4254547357559204, 0.5498191118240356, 0.5496659874916077, 0.5779644846916199, 0.5346126556396484, 0.438570499420166, 0.4164147973060608, 0.6110914945602417, 0.3093242049217224, 0.5974426865577698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.032663345336914})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.551611065864563})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4369315505027771})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42347121238708496})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3850055932998657})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3769221901893616})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42478781938552856})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.424554705619812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42006438970565796})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9554, 'crossentropy': 0.3196751953125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8361352682113647})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5482707619667053})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42932355403900146})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3733617663383484})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3259889483451843})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32918164134025574})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3170774579048157})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3125481903553009})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [45888, 55244, 36008, 33338, 24899, 22144, 45692, 15494, 59875, 59339], 'labels': [9, 7, 8, 8, 3, 0, 8, 7, -1, 1], 'scores': [0.338989794254303, 0.5870778560638428, 0.537792980670929, 0.47006773948669434, 0.3969467878341675, 0.3405439555644989, 0.4756251573562622, 0.5825017094612122, 0.3270092010498047, 0.3621903657913208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0251115560531616})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5818034410476685})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.431302011013031})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4452102780342102})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4085366725921631})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39476174116134644})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45184504985809326})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45607423782348633})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42379745841026306})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9559, 'crossentropy': 0.3573538818359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8813786506652832})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48550549149513245})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4060922861099243})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4034234285354614})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3482682704925537})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3562830090522766})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3303779363632202})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34513890743255615})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [58101, 6212, 48011, 44351, 57507, 22053, 41491, 35971, 8786, 24399], 'labels': [4, -1, -1, -1, 0, 5, 3, 0, 3, -1], 'scores': [0.4140589237213135, 0.28614985942840576, 0.37090349197387695, 0.29803991317749023, 0.6949366331100464, 0.5431470274925232, 0.4920390248298645, 0.7182167768478394, 0.4412307143211365, 0.4118901491165161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.890318751335144})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49100878834724426})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38043463230133057})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3705035448074341})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35960057377815247})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.374118447303772})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39532777667045593})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38575464487075806})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.3040039306640625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.794703483581543})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47957414388656616})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36479032039642334})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33551347255706787})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3071024417877197})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30713480710983276})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30326640605926514})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [14655, 32710, 5377, 706, 22272, 49563, 48355, 23185, 1189, 40654], 'labels': [3, -1, -1, -1, 5, 8, 3, -1, -1, -1], 'scores': [0.5327751636505127, 0.46514856815338135, 0.35425829887390137, 0.5007973909378052, 0.47054535150527954, 0.527671217918396, 0.5911439657211304, 0.42293334007263184, 0.2894477844238281, 0.4033573865890503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0541601181030273})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5297802090644836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3986866772174835})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4201456308364868})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3917143940925598})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39821183681488037})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4023294448852539})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4305388331413269})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.3380021484375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9058430194854736})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4632507562637329})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3685424327850342})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3388309180736542})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3107936978340149})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3055984675884247})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3174598813056946})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [55835, 31609, 19459, 43682, 15877, 18063, 59747, 53929, 30915, 40463], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, 3], 'scores': [0.4031982421875, 0.4991196393966675, 0.3632882833480835, 0.505591869354248, 0.39607346057891846, 0.42549604177474976, 0.40604013204574585, 0.3794255256652832, 0.4729684591293335, 0.38334327936172485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9254308938980103})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5088573694229126})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44518566131591797})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37692487239837646})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4163931608200073})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38524264097213745})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3754202723503113})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40690112113952637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4162256121635437})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39232444763183594})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9564, 'crossentropy': 0.32245830078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8329026699066162})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4749141335487366})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3857596516609192})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3594960570335388})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3345549404621124})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30838122963905334})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.298409104347229})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3054477274417877})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3018120527267456})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [12051, 16036, 132, 52089, 53693, 33740, 33505, 13942, 52214, 28518], 'labels': [-1, 8, 5, 7, 4, 4, 2, 4, 9, 4], 'scores': [0.3429248332977295, 0.3833456039428711, 0.3861621618270874, 0.4982911944389343, 0.46383965015411377, 0.5152906179428101, 0.6686038970947266, 0.5312116742134094, 0.4056876301765442, 0.5531526803970337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.945433497428894})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48707401752471924})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4225962162017822})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42170166969299316})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3981897830963135})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3774837851524353})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4016833007335663})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.39492011070251465})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4395145773887634})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.345777392578125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8285125494003296})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5036908388137817})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4086074233055115})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34696680307388306})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32875069975852966})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3316233158111572})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33791810274124146})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.345194548368454})
store['active_learning_steps'][36]['eval_training']['best_epoch']=5
store['active_learning_steps'][36]['acquisition']={'indices': [22613, 47909, 28536, 59653, 23733, 46996, 12131, 11028, 14208, 38998], 'labels': [7, 9, 3, 0, 5, 5, 9, -1, 9, -1], 'scores': [0.37224990129470825, 0.6135379672050476, 0.5923303365707397, 0.576766312122345, 0.3270184397697449, 0.5224922299385071, 0.500247061252594, 0.4807358980178833, 0.2530604600906372, 0.3906947374343872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0162549018859863})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5071508884429932})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4131896495819092})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39188241958618164})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39597731828689575})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36126095056533813})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36823248863220215})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3274914622306824})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3746151924133301})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35817477107048035})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3769112825393677})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.30154482421875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7883334159851074})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49102282524108887})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39268526434898376})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3419734239578247})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32811492681503296})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2754470705986023})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28744810819625854})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28641605377197266})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28666141629219055})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [49001, 37760, 1908, 46816, 6766, 30992, 51646, 38223, 45616, 49268], 'labels': [-1, -1, -1, 8, -1, -1, -1, -1, 5, -1], 'scores': [0.4683119058609009, 0.2558792233467102, 0.3845922350883484, 0.39940500259399414, 0.34244441986083984, 0.41521763801574707, 0.4011201858520508, 0.5249618291854858, 0.8297220468521118, 0.3733396530151367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0060728788375854})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6424587965011597})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4057331085205078})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38034170866012573})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40097689628601074})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3378170132637024})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4067613482475281})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3721432089805603})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.371872216463089})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.301546337890625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7596838474273682})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4809512794017792})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4219857454299927})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3669663369655609})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35424619913101196})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3088022470474243})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31157273054122925})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28944873809814453})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [25048, 28990, 16676, 29952, 40688, 27316, 5998, 50789, 36866, 50698], 'labels': [-1, 7, 3, -1, -1, 3, -1, 1, 6, 9], 'scores': [0.35943150520324707, 0.3874242901802063, 0.4054872989654541, 0.27169907093048096, 0.6108100414276123, 0.47126027941703796, 0.33759772777557373, 0.518008291721344, 0.400402307510376, 0.5481588840484619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0190834999084473})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5283641815185547})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4663848876953125})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41562503576278687})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4044836759567261})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34851738810539246})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37932026386260986})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38704967498779297})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3548547327518463})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.30062216796875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8959403038024902})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5151253342628479})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39883750677108765})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34119269251823425})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31910425424575806})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3069121241569519})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2931431233882904})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30122649669647217})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [32424, 27658, 40556, 7250, 23024, 18850, 58860, 12066, 8341, 22036], 'labels': [2, 0, 2, 3, 3, 2, -1, 8, -1, 2], 'scores': [0.44997796416282654, 0.4379088282585144, 0.43425196409225464, 0.3556196093559265, 0.3357257843017578, 0.32629403471946716, 0.3773195743560791, 0.5176263451576233, 0.34806251525878906, 0.30188143253326416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0454893112182617})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48529964685440063})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4279016852378845})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37643176317214966})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3720172643661499})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4024110436439514})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3609806001186371})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38437414169311523})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39576399326324463})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36978405714035034})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.305631640625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9006123542785645})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4765819311141968})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38934385776519775})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3134722113609314})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30322620272636414})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32911521196365356})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2667783796787262})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30488818883895874})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2821654975414276})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [45438, 28030, 10089, 6221, 59771, 44392, 36486, 31302, 18081, 24957], 'labels': [-1, 0, 6, 7, -1, -1, -1, 5, -1, -1], 'scores': [0.5340994596481323, 0.49716484546661377, 0.3443540334701538, 0.45276302099227905, 0.4804767370223999, 0.44237852096557617, 0.44095516204833984, 0.6545026302337646, 0.3405147194862366, 0.397403359413147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0331296920776367})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.554975152015686})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.378889799118042})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40899503231048584})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3712199926376343})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40186744928359985})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3947504758834839})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3778657615184784})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.315538623046875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8358371257781982})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4880698323249817})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41359853744506836})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36201947927474976})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35676246881484985})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3191816210746765})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31313973665237427})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [12651, 19663, 51987, 27952, 34920, 42496, 31370, 39678, 34706, 1282], 'labels': [9, -1, 3, 5, 9, -1, 1, -1, -1, 9], 'scores': [0.3909831643104553, 0.4755830764770508, 0.37745845317840576, 0.44120174646377563, 0.4675031900405884, 0.38103795051574707, 0.44564616680145264, 0.3214315176010132, 0.37014758586883545, 0.4211612939834595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0263500213623047})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5272380113601685})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41539210081100464})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37561988830566406})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3317965567111969})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3548765182495117})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32760363817214966})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3362491726875305})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38924986124038696})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33817195892333984})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2890637939453125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8415376543998718})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5052843689918518})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44695132970809937})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3658320903778076})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3125857710838318})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2993994355201721})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3078120946884155})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32320940494537354})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3067174553871155})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [53324, 24278, 15346, 25775, 55908, 52201, 21601, 33301, 10160, 18348], 'labels': [-1, 3, -1, -1, -1, -1, 1, -1, 7, 8], 'scores': [0.36526262760162354, 0.39548301696777344, 0.4110393524169922, 0.3683418035507202, 0.30663740634918213, 0.20331692695617676, 0.5605117678642273, 0.4408589005470276, 0.39409106969833374, 0.4846920967102051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0606800317764282})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.531151294708252})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4155808985233307})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3964948058128357})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3711150884628296})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39975428581237793})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36566221714019775})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40782058238983154})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3598698079586029})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3893905282020569})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3925101161003113})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37843671441078186})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.3005649658203125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.889143705368042})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5850329399108887})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40422168374061584})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3289045989513397})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32899582386016846})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3105795085430145})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.278671532869339})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29692918062210083})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27126947045326233})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26704075932502747})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27056512236595154})
store['active_learning_steps'][43]['eval_training']['best_epoch']=10
store['active_learning_steps'][43]['acquisition']={'indices': [4402, 34304, 15560, 47980, 38123, 31094, 21615, 32823, 11209, 44839], 'labels': [-1, 8, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5996750593185425, 0.660151481628418, 0.49219655990600586, 0.4041973352432251, 0.3910421133041382, 0.3519066572189331, 0.6386964321136475, 0.4904886484146118, 0.3842109441757202, 0.4705691337585449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.128751277923584})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5527204275131226})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39870792627334595})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3585600256919861})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34491828083992004})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37155604362487793})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3578674793243408})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35734909772872925})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.297953076171875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8812229633331299})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5158815979957581})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4394294023513794})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3685455918312073})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.357774555683136})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3657020926475525})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3678016662597656})
store['active_learning_steps'][44]['eval_training']['best_epoch']=5
store['active_learning_steps'][44]['acquisition']={'indices': [44998, 24659, 39444, 21381, 20050, 36167, 2036, 46626, 16027, 52613], 'labels': [4, -1, -1, -1, 9, -1, 4, 6, 2, -1], 'scores': [0.5682752132415771, 0.2545759677886963, 0.36639392375946045, 0.37947261333465576, 0.482258141040802, 0.3593103885650635, 0.3927684426307678, 0.52474445104599, 0.42566990852355957, 0.32900118827819824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1190569400787354})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.603966474533081})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39378440380096436})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3520100712776184})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36808061599731445})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33221620321273804})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3100980520248413})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3533703684806824})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3585820198059082})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3432384133338928})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2742084716796875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8167154788970947})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4860844612121582})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3464476764202118})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31698286533355713})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30640196800231934})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2966105043888092})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2663158178329468})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2699775695800781})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.282590389251709})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [14757, 52358, 32808, 47674, 19661, 37437, 30186, 50369, 52123, 12297], 'labels': [-1, 2, -1, -1, -1, 2, -1, 3, 9, 9], 'scores': [0.32417023181915283, 0.5907739400863647, 0.2581457495689392, 0.37645649909973145, 0.27579736709594727, 0.5614153146743774, 0.4206937551498413, 0.4620855450630188, 0.3881097435951233, 0.4434277415275574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1816558837890625})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5301951169967651})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4165304899215698})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37531962990760803})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39335018396377563})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3649228811264038})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34412163496017456})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35673999786376953})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36343804001808167})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3887791335582733})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2751826416015625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9283103942871094})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.537408709526062})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39464375376701355})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3448082208633423})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3215519189834595})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34129324555397034})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3044010400772095})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2692660987377167})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29509997367858887})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [36818, 53854, 14196, 20002, 31738, 53696, 52987, 17091, 30016, 7308], 'labels': [7, 8, 1, -1, 8, 5, -1, 4, 4, 8], 'scores': [0.5254157185554504, 0.5234671235084534, 0.28336018323898315, 0.22256559133529663, 0.5815955400466919, 0.5924721360206604, 0.31784236431121826, 0.4814215898513794, 0.5606998205184937, 0.4779912233352661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.212348461151123})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.608238935470581})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4441016912460327})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3922171890735626})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36424291133880615})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33391475677490234})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33549928665161133})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34678971767425537})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32700544595718384})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3437334895133972})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3521328568458557})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3532945513725281})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.292908544921875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9236029982566833})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5295882225036621})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36585551500320435})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34412121772766113})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2993149757385254})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3035876750946045})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2678188383579254})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27656611800193787})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2774977684020996})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27343595027923584})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [2908, 14290, 36985, 57408, 21671, 8505, 32048, 26472, 1522, 4537], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.49792981147766113, 0.3958306908607483, 0.6400517225265503, 0.31226837635040283, 0.47922396659851074, 0.520374596118927, 0.6875510811805725, 0.4651585817337036, 0.46105802059173584, 0.5554483532905579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0148184299468994})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.519632875919342})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43683677911758423})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3424624800682068})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3399130403995514})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34122908115386963})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3097079396247864})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3138554096221924})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35010477900505066})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32139143347740173})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2681801513671875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8261469006538391})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5062989592552185})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4030369520187378})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33961835503578186})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3207610547542572})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3137574791908264})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31309056282043457})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26753029227256775})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29453325271606445})
store['active_learning_steps'][48]['eval_training']['best_epoch']=8
store['active_learning_steps'][48]['acquisition']={'indices': [54376, 50236, 56695, 36260, 39473, 46817, 50897, 4322, 53019, 1403], 'labels': [-1, 0, 5, -1, -1, -1, 2, 2, 2, -1], 'scores': [0.4445688724517822, 0.5840799808502197, 0.38587576150894165, 0.3590104579925537, 0.41769111156463623, 0.3734945058822632, 0.23187363147735596, 0.29833436012268066, 0.6056655049324036, 0.3367912769317627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0910446643829346})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5660061240196228})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.445656418800354})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3438909947872162})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33926141262054443})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34196481108665466})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34519076347351074})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33770430088043213})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3285498023033142})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3437194526195526})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3501979112625122})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3683861494064331})
store['active_learning_steps'][49]['training']['best_epoch']=9
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.281405517578125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.0443322658538818})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5764172077178955})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40708616375923157})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3412046432495117})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3236521780490875})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2809457778930664})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2745663523674011})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2684839367866516})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2826678156852722})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27680423855781555})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2844715416431427})
store['active_learning_steps'][49]['eval_training']['best_epoch']=8
store['active_learning_steps'][49]['acquisition']={'indices': [50889, 11749, 28246, 1518, 5030, 51397, 40025, 48842, 40688, 2410], 'labels': [-1, -1, -1, 9, 8, -1, -1, 8, -1, 1], 'scores': [0.3136175274848938, 0.32949090003967285, 0.30343377590179443, 0.5679078698158264, 0.43918681144714355, 0.3143347501754761, 0.2775768041610718, 0.5033594369888306, 0.4897141456604004, 0.4742560386657715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.081667423248291})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5544923543930054})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.403542697429657})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3576895296573639})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3420172333717346})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3144938051700592})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3311871886253357})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34332647919654846})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37281548976898193})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.275742919921875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8455469608306885})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5147923231124878})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3645296096801758})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34473520517349243})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3287992477416992})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2964535355567932})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29024139046669006})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26019036769866943})
store['active_learning_steps'][50]['eval_training']['best_epoch']=8
store['active_learning_steps'][50]['acquisition']={'indices': [43475, 34114, 39686, 15080, 49309, 6208, 50912, 21203, 58398, 8381], 'labels': [-1, -1, -1, -1, -1, -1, 6, -1, -1, -1], 'scores': [0.3582463264465332, 0.3315899968147278, 0.3609774112701416, 0.3567906618118286, 0.4389420747756958, 0.4329092502593994, 0.3896465301513672, 0.30285680294036865, 0.48424410820007324, 0.3257330656051636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0521540641784668})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5202547311782837})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4562830328941345})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34989893436431885})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3679847717285156})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36049342155456543})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34831321239471436})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38018786907196045})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3540384769439697})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3420855700969696})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3813476860523224})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37868815660476685})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3638955056667328})
store['active_learning_steps'][51]['training']['best_epoch']=10
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2832553466796875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8980454206466675})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.522388219833374})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42488810420036316})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34250229597091675})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.321461021900177})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2967536449432373})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3162524700164795})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2681519091129303})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2856708765029907})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27176207304000854})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.309100866317749})
store['active_learning_steps'][51]['eval_training']['best_epoch']=8
store['active_learning_steps'][51]['acquisition']={'indices': [42428, 22779, 32880, 2508, 22293, 39320, 29530, 43427, 34847, 23526], 'labels': [5, 5, 0, -1, -1, 6, 4, -1, 0, 7], 'scores': [0.6083229780197144, 0.4171196222305298, 0.7136600613594055, 0.6476901173591614, 0.5130665302276611, 0.29995930194854736, 0.488900363445282, 0.6000782251358032, 0.4352838695049286, 0.6027585864067078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1750030517578125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6065413951873779})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39602333307266235})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3681373596191406})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32294541597366333})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3355259299278259})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3664752244949341})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33913689851760864})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.3007446533203125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8458656668663025})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5098754167556763})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39225536584854126})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37195533514022827})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3539431691169739})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31286925077438354})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34199827909469604})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [2372, 20849, 47697, 19840, 54000, 17526, 11433, 50343, 12197, 1477], 'labels': [-1, 3, -1, -1, -1, -1, -1, 6, -1, -1], 'scores': [0.5086910128593445, 0.42389053106307983, 0.38605237007141113, 0.5275981426239014, 0.34642744064331055, 0.37019336223602295, 0.2880204916000366, 0.4972337484359741, 0.46305596828460693, 0.34978950023651123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2090163230895996})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5484539270401001})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3931713104248047})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.382038414478302})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32968464493751526})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3267143964767456})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3326107859611511})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31284385919570923})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32975637912750244})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3449496030807495})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32666903734207153})
store['active_learning_steps'][53]['training']['best_epoch']=8
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.277896826171875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9664496183395386})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5154910683631897})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.43911248445510864})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33938610553741455})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32464224100112915})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30805703997612})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2850290834903717})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26941418647766113})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29935893416404724})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27261120080947876})
store['active_learning_steps'][53]['eval_training']['best_epoch']=8
store['active_learning_steps'][53]['acquisition']={'indices': [5904, 234, 16084, 39597, 10097, 2824, 38798, 53881, 34745, 54325], 'labels': [5, 0, 5, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5000067055225372, 0.5230927467346191, 0.5617395043373108, 0.29835987091064453, 0.3505392074584961, 0.3641270399093628, 0.4622570276260376, 0.4273790121078491, 0.2331409454345703, 0.4027407765388489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9540773034095764})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5070323348045349})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38229748606681824})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3107777237892151})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.321134090423584})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3072240650653839})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29628583788871765})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3057570457458496})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3441256582736969})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.330678790807724})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2535202880859375}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8348858952522278})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.49721384048461914})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34841471910476685})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2840704023838043})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28404855728149414})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2971802055835724})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28268975019454956})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2788201868534088})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28466251492500305})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [9897, 50555, 21923, 39031, 56019, 48045, 5987, 15366, 7673, 34824], 'labels': [-1, -1, -1, 2, -1, -1, -1, 8, -1, 9], 'scores': [0.37813329696655273, 0.6250286102294922, 0.555951714515686, 0.400243878364563, 0.4553440809249878, 0.44355952739715576, 0.40338945388793945, 0.3584306836128235, 0.5127712488174438, 0.36223316192626953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.34096097946167})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6645596027374268})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46761205792427063})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3756091594696045})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3806875944137573})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3515941798686981})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3048461675643921})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32641610503196716})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33317431807518005})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34414762258529663})
store['active_learning_steps'][55]['training']['best_epoch']=7
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.281598974609375}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8897653818130493})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5060425996780396})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3698100447654724})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.336919367313385})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.308752179145813})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32230329513549805})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.272905558347702})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28516659140586853})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2909328043460846})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [25801, 9979, 2765, 40022, 2764, 45501, 23718, 26850, 59358, 36550], 'labels': [-1, 2, 0, 8, -1, 2, 2, 2, -1, 9], 'scores': [0.45625805854797363, 0.40022414922714233, 0.5366500616073608, 0.5073535442352295, 0.24424004554748535, 0.5156064033508301, 0.49524301290512085, 0.44620150327682495, 0.3062955141067505, 0.4204676151275635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1259751319885254})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6106138825416565})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44203197956085205})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3587067723274231})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3488088846206665})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.338306725025177})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3500491976737976})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3574587404727936})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3066011071205139})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3611074686050415})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33404117822647095})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3401768207550049})
store['active_learning_steps'][56]['training']['best_epoch']=9
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2798688720703125}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8908036947250366})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43211185932159424})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41688036918640137})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33747246861457825})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28508102893829346})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2647007703781128})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26442641019821167})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3051510453224182})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25600916147232056})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2898831367492676})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25056880712509155})
store['active_learning_steps'][56]['eval_training']['best_epoch']=11
store['active_learning_steps'][56]['acquisition']={'indices': [19651, 7949, 10708, 32700, 34306, 12835, 21935, 4358, 37280, 53872], 'labels': [-1, -1, -1, -1, 9, -1, -1, -1, -1, 8], 'scores': [0.48574113845825195, 0.5699701309204102, 0.4957282543182373, 0.3941270112991333, 0.5099048018455505, 0.48283159732818604, 0.44236981868743896, 0.44034886360168457, 0.47850191593170166, 0.6318795084953308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.099351406097412})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.575225293636322})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41523557901382446})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31487759947776794})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3044579029083252})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2983136475086212})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32313793897628784})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3094930350780487})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29768091440200806})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33317530155181885})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3272239863872528})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3123570382595062})
store['active_learning_steps'][57]['training']['best_epoch']=9
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.2796646240234375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9026408195495605})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.526049017906189})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3489370048046112})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.350131630897522})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3030337691307068})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3161523938179016})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25956159830093384})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2856473922729492})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25869008898735046})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2674633860588074})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2760462760925293})
store['active_learning_steps'][57]['eval_training']['best_epoch']=9
store['active_learning_steps'][57]['acquisition']={'indices': [26615, 18486, 42927, 19030, 31398, 45047, 16572, 3118, 42281, 16203], 'labels': [-1, -1, -1, -1, -1, -1, 4, -1, -1, -1], 'scores': [0.38667774200439453, 0.49724817276000977, 0.43364405632019043, 0.4630277156829834, 0.33758723735809326, 0.4363229274749756, 0.5705756545066833, 0.39348793029785156, 0.5667513012886047, 0.5081835985183716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.138499140739441})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5390664339065552})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42088180780410767})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34090325236320496})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.338217556476593})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3087126612663269})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2894962430000305})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3049575388431549})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3111940622329712})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2830556333065033})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3604879379272461})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3871193826198578})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3629448413848877})
store['active_learning_steps'][58]['training']['best_epoch']=10
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2946703125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9298865795135498})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4970310926437378})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3580907881259918})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3033168911933899})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31765973567962646})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2914605736732483})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.292908251285553})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24271231889724731})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23156195878982544})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22919367253780365})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26786622405052185})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24312201142311096})
store['active_learning_steps'][58]['eval_training']['best_epoch']=10
store['active_learning_steps'][58]['acquisition']={'indices': [7168, 45554, 34352, 11339, 22974, 24130, 28397, 51146, 13407, 55582], 'labels': [8, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.7109016180038452, 0.41810786724090576, 0.5088651180267334, 0.40539097785949707, 0.511210560798645, 0.4198789596557617, 0.4736020565032959, 0.369717001914978, 0.39693206548690796, 0.3535001277923584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0862092971801758})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5903152227401733})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4174003601074219})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35249969363212585})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3089115023612976})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3043682873249054})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29701900482177734})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33545392751693726})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3157282769680023})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3634621500968933})
store['active_learning_steps'][59]['training']['best_epoch']=7
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2546080322265625}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0154448747634888})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5738512277603149})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4245043694972992})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3731212317943573})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29802262783050537})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3017960488796234})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3225673735141754})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28793734312057495})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3181924819946289})
store['active_learning_steps'][59]['eval_training']['best_epoch']=8
store['active_learning_steps'][59]['acquisition']={'indices': [682, 41872, 150, 36894, 20709, 1695, 7847, 27998, 55082, 16792], 'labels': [-1, -1, 4, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.5115559101104736, 0.2198411226272583, 0.33449167013168335, 0.38959020376205444, 0.4795151352882385, 0.2953307628631592, 0.43444812297821045, 0.512702465057373, 0.23857927322387695, 0.3624293804168701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1521074771881104})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5552653074264526})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.45082008838653564})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33308592438697815})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3618481159210205})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3459818959236145})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3255401849746704})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30812588334083557})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32934513688087463})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35348039865493774})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3174592852592468})
store['active_learning_steps'][60]['training']['best_epoch']=8
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2614437255859375}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9284338355064392})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4815675616264343})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3868674039840698})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3431432247161865})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2950299382209778})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2987867295742035})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26780813932418823})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2674873173236847})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26742690801620483})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27665388584136963})
store['active_learning_steps'][60]['eval_training']['best_epoch']=9
store['active_learning_steps'][60]['acquisition']={'indices': [39164, 46524, 44534, 40166, 29432, 17365, 9322, 55778, 39429, 17341], 'labels': [-1, 6, 9, -1, -1, 0, 0, -1, 2, -1], 'scores': [0.41752928495407104, 0.4943388104438782, 0.4659540057182312, 0.3829820156097412, 0.3854508399963379, 0.5921868085861206, 0.2905418276786804, 0.4461127519607544, 0.6074386239051819, 0.4297570586204529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0748968124389648})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5233011245727539})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38778063654899597})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3138062357902527})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29780155420303345})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2758704423904419})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30356764793395996})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3002144694328308})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3139854371547699})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.258914794921875}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8809100389480591})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5642602443695068})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39246994256973267})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32864195108413696})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31783175468444824})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2803981900215149})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32104241847991943})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2861286997795105})
store['active_learning_steps'][61]['eval_training']['best_epoch']=6
store['active_learning_steps'][61]['acquisition']={'indices': [32608, 44208, 55520, 45906, 43864, 32000, 38835, 34408, 12051, 52376], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3588000535964966, 0.37690162658691406, 0.29654908180236816, 0.4103052616119385, 0.3745919466018677, 0.4025075435638428, 0.377400279045105, 0.45968878269195557, 0.5527613162994385, 0.40584635734558105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1620385646820068})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5626348257064819})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4095909297466278})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34376752376556396})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3323923945426941})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29649823904037476})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3195172846317291})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30105963349342346})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3052593171596527})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2725391845703125}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9410082697868347})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5451624989509583})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4338781237602234})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3621426224708557})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32978731393814087})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31871819496154785})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3159729242324829})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32235127687454224})
store['active_learning_steps'][62]['eval_training']['best_epoch']=7
store['active_learning_steps'][62]['acquisition']={'indices': [5666, 29099, 5974, 59957, 32504, 29926, 14100, 19927, 40767, 42634], 'labels': [-1, -1, -1, 3, -1, -1, 5, -1, -1, -1], 'scores': [0.493041455745697, 0.3757238984107971, 0.3109515309333801, 0.3182470202445984, 0.3717074394226074, 0.41186773777008057, 0.384014368057251, 0.3306610584259033, 0.4507730007171631, 0.3737204074859619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.196035623550415})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5934144258499146})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38769400119781494})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.37104159593582153})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33661380410194397})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3251327574253082})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2977118492126465})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3050997257232666})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3156452178955078})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30314451456069946})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2858585693359375}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9473721385002136})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4745931029319763})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3891928791999817})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37082934379577637})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32296863198280334})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2907252907752991})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30412065982818604})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29552435874938965})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2907314598560333})
store['active_learning_steps'][63]['eval_training']['best_epoch']=6
store['active_learning_steps'][63]['acquisition']={'indices': [10982, 50366, 35808, 27031, 22567, 32664, 42153, 38361, 45602, 23154], 'labels': [1, 5, -1, -1, 3, -1, -1, -1, 5, 0], 'scores': [0.4096605181694031, 0.29527711868286133, 0.25736451148986816, 0.28214824199676514, 0.4683024287223816, 0.38383758068084717, 0.2951171398162842, 0.39128541946411133, 0.6024829149246216, 0.5188044905662537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1074286699295044})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5273237228393555})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38804537057876587})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33466553688049316})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31450915336608887})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3066488206386566})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33171898126602173})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2834817171096802})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3371697962284088})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31906577944755554})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3000292181968689})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.271486474609375}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8530593514442444})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4738002419471741})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.336739182472229})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28595981001853943})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3077881932258606})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2745223641395569})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29049476981163025})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26203468441963196})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26962172985076904})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.244267076253891})
store['active_learning_steps'][64]['eval_training']['best_epoch']=10
store['active_learning_steps'][64]['acquisition']={'indices': [9279, 37347, 13969, 31926, 34951, 21629, 32825, 12836, 25118, 32573], 'labels': [-1, 2, 3, -1, 7, -1, -1, 3, -1, 8], 'scores': [0.5863557457923889, 0.6226264536380768, 0.717145562171936, 0.52653568983078, 0.2552819550037384, 0.43278783559799194, 0.5636999011039734, 0.47765499353408813, 0.45323991775512695, 0.5603736639022827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2311205863952637})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6970551013946533})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4236404299736023})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34810423851013184})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3549051284790039})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3463115394115448})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35043251514434814})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2978112995624542})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2989189624786377})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2915322482585907})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.31162887811660767})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31351596117019653})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3331616520881653})
store['active_learning_steps'][65]['training']['best_epoch']=10
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.265414111328125}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0106136798858643})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5402883291244507})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4078269600868225})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33098095655441284})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2636021673679352})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2858416736125946})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28439861536026})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25662919878959656})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2604079246520996})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2408258616924286})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25134748220443726})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2502540946006775})
store['active_learning_steps'][65]['eval_training']['best_epoch']=10
store['active_learning_steps'][65]['acquisition']={'indices': [21851, 11856, 5310, 31246, 29271, 36436, 42953, 58636, 51404, 44062], 'labels': [-1, -1, -1, -1, -1, -1, 4, -1, -1, -1], 'scores': [0.44265222549438477, 0.3451039791107178, 0.38398313522338867, 0.4898759126663208, 0.41620302200317383, 0.5044959187507629, 0.5504451394081116, 0.47782254219055176, 0.4077965021133423, 0.46396851539611816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.3380258083343506})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5238754749298096})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38910922408103943})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3154207468032837})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3165675401687622})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.300397664308548})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29619115591049194})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30530786514282227})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.30079442262649536})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28325170278549194})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2973342537879944})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.36102670431137085})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32699456810951233})
store['active_learning_steps'][66]['training']['best_epoch']=10
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.2525939208984375}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9833815097808838})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47016629576683044})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38707855343818665})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2959575057029724})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32732319831848145})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28662973642349243})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27796944975852966})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25214964151382446})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2652552127838135})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24810492992401123})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23236116766929626})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.20391733944416046})
store['active_learning_steps'][66]['eval_training']['best_epoch']=12
store['active_learning_steps'][66]['acquisition']={'indices': [9126, 49664, 33027, 30127, 23974, 29439, 14994, 11298, 42661, 38389], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 7], 'scores': [0.4475889801979065, 0.5146463513374329, 0.5051548480987549, 0.4615575075149536, 0.4191330671310425, 0.35064029693603516, 0.3564755916595459, 0.37042224407196045, 0.4890921115875244, 0.5461047291755676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4434056282043457})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5851626396179199})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38976818323135376})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3758533000946045})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3311777114868164})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.339243620634079})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33390504121780396})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3575918674468994})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9608, 'crossentropy': 0.3065676025390625}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8847898840904236})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5689863562583923})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3899967074394226})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3739796280860901})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36102259159088135})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34150099754333496})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3489620089530945})
store['active_learning_steps'][67]['eval_training']['best_epoch']=6
store['active_learning_steps'][67]['acquisition']={'indices': [39737, 3990, 9552, 59389, 59344, 57720, 4822, 7647, 54950, 46442], 'labels': [-1, -1, 0, -1, 9, 0, 4, -1, 8, -1], 'scores': [0.31784212589263916, 0.30217838287353516, 0.6563044190406799, 0.36762046813964844, 0.5771757960319519, 0.44149112701416016, 0.6754039525985718, 0.37954187393188477, 0.6000140309333801, 0.3027890920639038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.122423768043518})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5609723925590515})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41531482338905334})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3295878767967224})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29467475414276123})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3022354245185852})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2893896698951721})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3120717406272888})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3100450038909912})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3027588427066803})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.284187890625}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8895813226699829})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45494478940963745})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40625613927841187})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3508099317550659})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3077247142791748})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2919040322303772})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2902294993400574})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2836776375770569})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24227666854858398})
store['active_learning_steps'][68]['eval_training']['best_epoch']=9
store['active_learning_steps'][68]['acquisition']={'indices': [4642, 55188, 53675, 37078, 27393, 58626, 52851, 41490, 1586, 9472], 'labels': [0, 2, 5, 8, -1, -1, 2, 0, 7, 2], 'scores': [0.2904675304889679, 0.4233592748641968, 0.27472954988479614, 0.4721055030822754, 0.4193516969680786, 0.38311469554901123, 0.4489877223968506, 0.47173744440078735, 0.46100759506225586, 0.4334094524383545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.264062523841858})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6629588603973389})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3994130492210388})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33775484561920166})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3051622211933136})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28962230682373047})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3053584098815918})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2792653441429138})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31492185592651367})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3219871520996094})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32996582984924316})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2665562255859375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9553308486938477})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5092843770980835})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35728275775909424})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36142271757125854})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3373259902000427})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2994041442871094})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3224264085292816})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.305353581905365})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2822505831718445})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2594892382621765})
store['active_learning_steps'][69]['eval_training']['best_epoch']=10
store['active_learning_steps'][69]['acquisition']={'indices': [45700, 31559, 33735, 19517, 35477, 19662, 6859, 577, 58818, 173], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.41808152198791504, 0.4897650480270386, 0.3387718200683594, 0.4452788233757019, 0.5021005868911743, 0.5284625887870789, 0.41154932975769043, 0.5249618887901306, 0.4677931070327759, 0.44093263149261475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.111387848854065})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5926051735877991})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4203205704689026})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33912158012390137})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3208240270614624})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3128952085971832})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30223068594932556})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3274833559989929})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30991554260253906})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3282683491706848})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2622134033203125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9357582330703735})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.501244306564331})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40772342681884766})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38527578115463257})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33078595995903015})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32873794436454773})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29069948196411133})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28891316056251526})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2833985686302185})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [12880, 50425, 53847, 14427, 40445, 21517, 47938, 21042, 28306, 4961], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.5665720701217651, 0.541193425655365, 0.47085487842559814, 0.46549129486083984, 0.4720425605773926, 0.46151089668273926, 0.3631424307823181, 0.6551933884620667, 0.44648277759552, 0.48405760526657104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.242638111114502})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5664988160133362})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4512309432029724})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39402803778648376})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3408239483833313})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3615419864654541})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32409170269966125})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3586956262588501})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3264259696006775})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34540438652038574})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2967513916015625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9298137426376343})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5651522874832153})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40397828817367554})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3530399799346924})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35070180892944336})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31018757820129395})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3006879985332489})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30863142013549805})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30141985416412354})
store['active_learning_steps'][71]['eval_training']['best_epoch']=7
store['active_learning_steps'][71]['acquisition']={'indices': [27858, 48735, 58047, 1995, 46654, 30493, 45315, 36524, 36482, 58661], 'labels': [-1, -1, -1, -1, 0, 1, -1, -1, -1, -1], 'scores': [0.43999338150024414, 0.5360062122344971, 0.3708847761154175, 0.45857298374176025, 0.5106597542762756, 0.5358874797821045, 0.3492404818534851, 0.43275725841522217, 0.5859545469284058, 0.2967027425765991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2568511962890625})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6981624364852905})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4736345410346985})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4077188968658447})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36441612243652344})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3383252024650574})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3536418080329895})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32364049553871155})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31947416067123413})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.356048583984375})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3351452052593231})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2960803806781769})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3310621976852417})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3429658114910126})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3880128562450409})
store['active_learning_steps'][72]['training']['best_epoch']=12
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.26141484375}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8683083653450012})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5811405181884766})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4263930916786194})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35513466596603394})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33326101303100586})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29147177934646606})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2826654016971588})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26558277010917664})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.254805326461792})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27694085240364075})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2742881774902344})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25685346126556396})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [6237, 57300, 40517, 56898, 23749, 34660, 55648, 56534, 3895, 12427], 'labels': [-1, -1, -1, -1, -1, 3, 9, -1, -1, 4], 'scores': [0.32611262798309326, 0.577186107635498, 0.43870246410369873, 0.5677847862243652, 0.4446984529495239, 0.47552281618118286, 0.3951845169067383, 0.5153695344924927, 0.5772719383239746, 0.3414456844329834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2253386974334717})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.60300213098526})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4584185481071472})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37379926443099976})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3281395435333252})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3309880495071411})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3249102234840393})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3272920846939087})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33451133966445923})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3616202771663666})
store['active_learning_steps'][73]['training']['best_epoch']=7
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2650383056640625}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9995900392532349})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.522577702999115})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40564805269241333})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3457612991333008})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31949758529663086})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.314639151096344})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33812668919563293})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2982385754585266})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27975666522979736})
store['active_learning_steps'][73]['eval_training']['best_epoch']=9
store['active_learning_steps'][73]['acquisition']={'indices': [40893, 15320, 49515, 22583, 295, 24146, 26822, 12200, 6044, 21765], 'labels': [-1, -1, 2, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.3810819387435913, 0.3380817174911499, 0.4023474454879761, 0.4020332098007202, 0.35951000452041626, 0.40356600284576416, 0.42068564891815186, 0.3221259117126465, 0.39313769340515137, 0.44783008098602295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.1660380363464355})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5913697481155396})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.44236600399017334})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3881347179412842})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3355160355567932})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31519144773483276})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3229104280471802})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32010000944137573})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31296277046203613})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3240519165992737})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29278916120529175})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3154172897338867})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3009350299835205})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3461255431175232})
store['active_learning_steps'][74]['training']['best_epoch']=11
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2671354248046875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9405121803283691})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4985083341598511})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4075731337070465})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32497695088386536})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29889005422592163})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2718580365180969})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2693859040737152})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26825040578842163})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25122320652008057})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25319668650627136})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2328806221485138})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24958786368370056})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23968631029129028})
store['active_learning_steps'][74]['eval_training']['best_epoch']=11
store['active_learning_steps'][74]['acquisition']={'indices': [33582, 24659, 40311, 29749, 564, 35299, 787, 59720, 2150, 31364], 'labels': [-1, -1, -1, 5, 4, -1, -1, -1, 8, -1], 'scores': [0.43231141567230225, 0.3015033006668091, 0.436792254447937, 0.6828639507293701, 0.21046487987041473, 0.499944806098938, 0.41047418117523193, 0.30079972743988037, 0.4087315797805786, 0.3278982639312744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1328113079071045})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6229226589202881})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3870556950569153})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3657417595386505})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.317795991897583})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31954073905944824})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29046201705932617})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31084269285202026})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27821463346481323})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2871803045272827})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26602083444595337})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3173861801624298})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28625065088272095})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37291276454925537})
store['active_learning_steps'][75]['training']['best_epoch']=11
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.24667958984375}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9235275387763977})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5319067239761353})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3829830288887024})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3348352313041687})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3139355182647705})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24652203917503357})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2833879590034485})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.274444043636322})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2688690423965454})
store['active_learning_steps'][75]['eval_training']['best_epoch']=6
store['active_learning_steps'][75]['acquisition']={'indices': [26017, 1925, 39411, 31385, 9850, 22139, 38061, 16853, 50415, 9098], 'labels': [5, -1, -1, -1, -1, 2, 2, -1, -1, 2], 'scores': [0.4589846134185791, 0.5027570724487305, 0.3159099817276001, 0.39273738861083984, 0.2303677797317505, 0.3669310212135315, 0.456977903842926, 0.6504113078117371, 0.46951353549957275, 0.5002927780151367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.245185136795044})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5636214017868042})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47150248289108276})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4008898437023163})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3309309184551239})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34064120054244995})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2971053719520569})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3122522830963135})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31826251745224})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3151692748069763})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.25136708984375}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9304246306419373})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5291271805763245})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38746604323387146})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3360649347305298})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29398834705352783})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2782152593135834})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2811774015426636})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25771644711494446})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2658158540725708})
store['active_learning_steps'][76]['eval_training']['best_epoch']=8
store['active_learning_steps'][76]['acquisition']={'indices': [7984, 35315, 34966, 47304, 6262, 42085, 14355, 27234, 52646, 26300], 'labels': [4, -1, -1, -1, -1, -1, -1, -1, 9, 0], 'scores': [0.509388267993927, 0.2819138765335083, 0.4026552438735962, 0.2643454074859619, 0.3969022035598755, 0.518848180770874, 0.34864741563796997, 0.33052825927734375, 0.5181697607040405, 0.37597256898880005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3275375366210938})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6772099137306213})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.48479345440864563})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3881208598613739})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35699111223220825})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.337327778339386})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3179347515106201})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30213943123817444})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3205846846103668})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33376723527908325})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35390937328338623})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2507410400390625}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9172255992889404})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4997807741165161})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.408393919467926})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35401156544685364})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2870115041732788})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29026421904563904})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2836122512817383})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3483518660068512})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30517131090164185})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2798711657524109})
store['active_learning_steps'][77]['eval_training']['best_epoch']=10
store['active_learning_steps'][77]['acquisition']={'indices': [7759, 35804, 5440, 37638, 52014, 20839, 46979, 42646, 41156, 35269], 'labels': [-1, 9, -1, -1, 3, -1, -1, -1, 0, -1], 'scores': [0.45156145095825195, 0.5168910622596741, 0.5938695669174194, 0.3646194338798523, 0.4188040494918823, 0.25477051734924316, 0.334179162979126, 0.44893330335617065, 0.31535398960113525, 0.5197951793670654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2959649562835693})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.6282632946968079})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47271230816841125})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.306043416261673})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3422180414199829})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.289944589138031})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30189985036849976})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3106535077095032})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3032434582710266})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.2639651611328125}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0209202766418457})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5017736554145813})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41684943437576294})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33822137117385864})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.37928450107574463})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29565519094467163})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3389403223991394})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29218024015426636})
store['active_learning_steps'][78]['eval_training']['best_epoch']=8
store['active_learning_steps'][78]['acquisition']={'indices': [28266, 56378, 56800, 20720, 28810, 17663, 29646, 13733, 24090, 1277], 'labels': [-1, -1, -1, 7, -1, -1, -1, -1, -1, 1], 'scores': [0.38563597202301025, 0.32287275791168213, 0.4675569534301758, 0.42707300186157227, 0.4176614284515381, 0.2748093605041504, 0.4442845582962036, 0.35964149236679077, 0.4079935550689697, 0.30068695545196533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1386051177978516})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5646960139274597})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.39706283807754517})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3146437406539917})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32990819215774536})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3004499077796936})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29456597566604614})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3139262795448303})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.286213755607605})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3054664731025696})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3146733045578003})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30512070655822754})
store['active_learning_steps'][79]['training']['best_epoch']=9
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.267275830078125}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0413483381271362})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5621277093887329})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42086514830589294})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33661890029907227})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29765716195106506})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.286712110042572})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26286178827285767})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2505337595939636})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23187407851219177})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2677943706512451})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25417494773864746})
store['active_learning_steps'][79]['eval_training']['best_epoch']=9
store['active_learning_steps'][79]['acquisition']={'indices': [5691, 10241, 56482, 41593, 33812, 36235, 59868, 8281, 52140, 29944], 'labels': [1, 4, -1, 2, 6, -1, -1, 4, 4, 6], 'scores': [0.3254122734069824, 0.39022791385650635, 0.40611445903778076, 0.4815730154514313, 0.544109582901001, 0.41802477836608887, 0.5693213939666748, 0.3767479956150055, 0.5485354065895081, 0.4632054269313812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2223036289215088})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5909836292266846})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4332970380783081})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33071643114089966})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30374598503112793})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2750065326690674})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2532549798488617})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2726106643676758})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30013081431388855})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2656051814556122})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.2592845947265625}
