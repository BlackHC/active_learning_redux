store = {}
store['timestamp']=1620294907
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=4']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=40
store['config']={'seed': 5, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.044506788253784})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.55367112159729})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5569536685943604})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7237491607666016})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6873, 'crossentropy': 2.010672265625}
store['active_learning_steps'][0]['acquisition']={'indices': [58168, 47651, 14825, 36150, 52785], 'labels': [8, 3, 3, 7, 3], 'scores': [1.1433364152908325, 1.1396369934082031, 1.1332383155822754, 1.1294299364089966, 1.1239758729934692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0498838424682617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.369986057281494})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.7068891525268555})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.889873504638672})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7244, 'crossentropy': 1.953999609375}
store['active_learning_steps'][1]['acquisition']={'indices': [5730, 57542, 47322, 33331, 7923], 'labels': [0, 0, 8, 3, 8], 'scores': [1.2048892378807068, 1.1946399807929993, 1.1933009624481201, 1.1909216046333313, 1.1879906058311462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.013514280319214})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7621662616729736})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.633269786834717})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.8849802017211914})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7046, 'crossentropy': 1.7492642578125}
store['active_learning_steps'][2]['acquisition']={'indices': [34457, 50538, 58812, 39431, 58811], 'labels': [0, 2, 3, 6, 2], 'scores': [1.0084202289581299, 1.0004808902740479, 0.9990029335021973, 0.986118495464325, 0.9849538207054138]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.039179801940918})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1953563690185547})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.6438651084899902})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.702220916748047})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6941, 'crossentropy': 1.80638828125}
store['active_learning_steps'][3]['acquisition']={'indices': [6025, 30174, 55053, 10371, 39182], 'labels': [4, 4, 4, 4, 4], 'scores': [1.014618694782257, 1.0106558203697205, 1.0052390098571777, 0.9966810345649719, 0.9944851994514465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.024758815765381})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6128153800964355})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5701377391815186})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.7818970680236816})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7099, 'crossentropy': 1.920413671875}
store['active_learning_steps'][4]['acquisition']={'indices': [22802, 48030, 48752, 5170, 40473], 'labels': [5, 9, 8, 8, 5], 'scores': [1.1090896725654602, 1.092180848121643, 1.091741919517517, 1.0902655124664307, 1.0897610783576965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6723628044128418})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.8642863035202026})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.187373161315918})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.0312585830688477})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7375, 'crossentropy': 1.43065}
store['active_learning_steps'][5]['acquisition']={'indices': [36335, 7895, 44733, 40088, 813], 'labels': [2, 2, 5, 5, 2], 'scores': [0.9253677129745483, 0.9169037342071533, 0.9140296578407288, 0.9133411645889282, 0.9114103317260742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6155893802642822})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8481602668762207})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.049281597137451})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.233577251434326})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7494, 'crossentropy': 1.44564736328125}
store['active_learning_steps'][6]['acquisition']={'indices': [27130, 19276, 9468, 8968, 36122], 'labels': [9, 6, 6, 9, 9], 'scores': [1.017428696155548, 1.0113770961761475, 0.9529725313186646, 0.9405134320259094, 0.9398849606513977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2568058967590332})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.4652056694030762})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.5897873640060425})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.8156660795211792})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7862, 'crossentropy': 1.11901806640625}
store['active_learning_steps'][7]['acquisition']={'indices': [34758, 25309, 19942, 8661, 12934], 'labels': [8, 2, 5, 8, 8], 'scores': [0.9576938152313232, 0.9304380416870117, 0.9253116250038147, 0.9216768741607666, 0.9213947057723999]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.464859962463379})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.5008028745651245})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.7922426462173462})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8104138374328613})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7497, 'crossentropy': 1.307343359375}
store['active_learning_steps'][8]['acquisition']={'indices': [47787, 3772, 10497, 1724, 2337], 'labels': [2, 6, 2, 2, 2], 'scores': [0.9701537489891052, 0.9400238394737244, 0.9399731159210205, 0.9316843748092651, 0.925193190574646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2478352785110474})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.540283203125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.6038382053375244})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6141633987426758})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7793, 'crossentropy': 1.1097982421875}
store['active_learning_steps'][9]['acquisition']={'indices': [11616, 37769, 32662, 12903, 12305], 'labels': [7, 7, 7, 9, 9], 'scores': [0.9114295840263367, 0.9110751152038574, 0.8739654421806335, 0.8721879124641418, 0.8697096109390259]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0877007246017456})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1712117195129395})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3651111125946045})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.3002912998199463})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.808, 'crossentropy': 0.96791650390625}
store['active_learning_steps'][10]['acquisition']={'indices': [17756, 59361, 39407, 31014, 3524], 'labels': [8, 8, 0, 8, 6], 'scores': [0.8444655537605286, 0.8403865098953247, 0.8184574246406555, 0.8141668438911438, 0.811976432800293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.082911491394043})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1716456413269043})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1809289455413818})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2936525344848633})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7819, 'crossentropy': 1.02131328125}
store['active_learning_steps'][11]['acquisition']={'indices': [59333, 14395, 31624, 54065, 2801], 'labels': [2, 7, 9, 7, 4], 'scores': [0.8605901002883911, 0.8057153224945068, 0.8020377159118652, 0.800330638885498, 0.788572371006012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1273796558380127})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2761785984039307})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.2100481986999512})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3866541385650635})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7707, 'crossentropy': 1.10164990234375}
store['active_learning_steps'][12]['acquisition']={'indices': [41999, 45794, 37447, 27077, 15432], 'labels': [0, 4, 4, 4, 4], 'scores': [0.8050898313522339, 0.7831339240074158, 0.7718727588653564, 0.7450818419456482, 0.7416744232177734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8667278289794922})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8891701102256775})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8858255743980408})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1416008472442627})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8526, 'crossentropy': 0.793127392578125}
store['active_learning_steps'][13]['acquisition']={'indices': [7033, 50233, 52866, 2118, 16860], 'labels': [7, 7, 7, 7, 8], 'scores': [0.8174717426300049, 0.8011522889137268, 0.7972687482833862, 0.7944865226745605, 0.7757983803749084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0428173542022705})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0554851293563843})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2144265174865723})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2029361724853516})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7947, 'crossentropy': 0.96619072265625}
store['active_learning_steps'][14]['acquisition']={'indices': [23104, 28455, 24426, 45047, 28930], 'labels': [0, 5, 5, 2, 7], 'scores': [0.741759181022644, 0.7081895470619202, 0.7007843255996704, 0.6898398399353027, 0.6890524625778198]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0401403903961182})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9602601528167725})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1379868984222412})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.107703447341919})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1203199625015259})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8288, 'crossentropy': 0.90690283203125}
store['active_learning_steps'][15]['acquisition']={'indices': [31761, 12345, 16600, 39146, 11675], 'labels': [4, 3, 4, 2, 0], 'scores': [0.9585064649581909, 0.9343604445457458, 0.9054888486862183, 0.8823758959770203, 0.8805940747261047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0528967380523682})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.028530240058899})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2022219896316528})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9993616342544556})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2304977178573608})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1783201694488525})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3872164487838745})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8446, 'crossentropy': 0.9290798828125}
store['active_learning_steps'][16]['acquisition']={'indices': [20171, 32533, 19590, 7768, 15893], 'labels': [5, 5, 5, 8, 5], 'scores': [1.0561634302139282, 1.0307298302650452, 1.0296591520309448, 1.0170294642448425, 1.0142058730125427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0777690410614014})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.063835859298706})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0514800548553467})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.954071044921875})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1500802040100098})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.110837459564209})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2224466800689697})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8645, 'crossentropy': 0.81750478515625}
store['active_learning_steps'][17]['acquisition']={'indices': [51180, 26742, 31558, 48096, 26600], 'labels': [7, 7, 7, 7, 7], 'scores': [1.2310316562652588, 1.1224603652954102, 1.1183610558509827, 1.1147382855415344, 1.0828105807304382]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1537249088287354})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9904312491416931})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1329545974731445})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3159453868865967})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.417905330657959})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.835, 'crossentropy': 0.8749455078125}
store['active_learning_steps'][18]['acquisition']={'indices': [18598, 47132, 49992, 59747, 19586], 'labels': [9, 2, 5, 5, 9], 'scores': [1.0435301661491394, 0.9168879985809326, 0.8932880163192749, 0.8748358488082886, 0.8744843006134033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0367127656936646})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0050973892211914})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0367841720581055})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1162748336791992})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.293427586555481})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8317, 'crossentropy': 0.91973232421875}
store['active_learning_steps'][19]['acquisition']={'indices': [21946, 13743, 16298, 16084, 46476], 'labels': [3, 2, 2, 5, 5], 'scores': [0.902321994304657, 0.8979412913322449, 0.88763028383255, 0.8838695883750916, 0.8830752372741699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0739766359329224})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9376206398010254})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0672457218170166})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0563899278640747})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1540656089782715})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8362, 'crossentropy': 0.8435623046875}
store['active_learning_steps'][20]['acquisition']={'indices': [21880, 5684, 23262, 17494, 9118], 'labels': [2, 6, 9, 5, 9], 'scores': [0.9414617419242859, 0.905460774898529, 0.8774911761283875, 0.8759671449661255, 0.8678120970726013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1424720287322998})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9402398467063904})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9812541007995605})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0316847562789917})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.030767560005188})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8341, 'crossentropy': 0.7993453125}
store['active_learning_steps'][21]['acquisition']={'indices': [48507, 21840, 56990, 56391, 51231], 'labels': [6, 9, 5, 3, 5], 'scores': [0.8650643229484558, 0.8516868948936462, 0.8504687547683716, 0.8174320459365845, 0.8161486387252808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1283812522888184})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9609498381614685})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8867330551147461})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9676549434661865})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1934986114501953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0548315048217773})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.851, 'crossentropy': 0.809785400390625}
store['active_learning_steps'][22]['acquisition']={'indices': [37154, 51432, 134, 28420, 35628], 'labels': [1, 1, 1, 1, 5], 'scores': [1.0232877135276794, 0.9947457909584045, 0.9778622388839722, 0.9692167639732361, 0.9674334526062012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2092597484588623})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.979709267616272})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0816688537597656})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1296905279159546})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.028098225593567})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8357, 'crossentropy': 0.858140625}
store['active_learning_steps'][23]['acquisition']={'indices': [9180, 424, 40390, 20745, 49252], 'labels': [3, 9, 0, 6, 6], 'scores': [0.9090418219566345, 0.8662886023521423, 0.8597370386123657, 0.8505853414535522, 0.8497991561889648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1424106359481812})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.86388099193573})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8773977756500244})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0015124082565308})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.992311418056488})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8584, 'crossentropy': 0.7600458984375}
store['active_learning_steps'][24]['acquisition']={'indices': [21304, 29132, 39429, 26444, 35946], 'labels': [4, 8, 2, 1, 4], 'scores': [0.8025627732276917, 0.787627100944519, 0.7853358387947083, 0.7816261053085327, 0.7715638279914856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0285767316818237})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8091533184051514})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8261093497276306})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9300867319107056})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9095523357391357})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8591, 'crossentropy': 0.72733984375}
store['active_learning_steps'][25]['acquisition']={'indices': [26358, 18398, 34520, 7949, 3719], 'labels': [3, 4, 6, -1, 2], 'scores': [0.9776327610015869, 0.9538435339927673, 0.9329382181167603, 0.9256665706634521, 0.8925847411155701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0608673095703125})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8143189549446106})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7636746764183044})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7746697664260864})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7605738043785095})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8907613754272461})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8266357183456421})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9278005361557007})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8863, 'crossentropy': 0.695636767578125}
store['active_learning_steps'][26]['acquisition']={'indices': [53187, 32535, 49473, 11943, 8445], 'labels': [1, 1, 1, 1, 1], 'scores': [1.1288527250289917, 1.097395896911621, 1.0769838094711304, 1.0737394094467163, 1.0688769817352295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0695455074310303})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6662976741790771})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7280768156051636})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6162999868392944})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8258117437362671})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7718379497528076})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.801586389541626})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.562507958984375}
store['active_learning_steps'][27]['acquisition']={'indices': [31658, 57507, 7146, 3810, 6974], 'labels': [2, 0, 2, 3, 2], 'scores': [0.9766803979873657, 0.971611499786377, 0.9690380096435547, 0.9687760472297668, 0.9572663903236389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.035585641860962})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.733084499835968})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8116214871406555})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7975713610649109})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8734524250030518})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.651174267578125}
store['active_learning_steps'][28]['acquisition']={'indices': [17592, 47068, 36744, 2856, 10937], 'labels': [4, 4, 1, 4, 4], 'scores': [0.8989278078079224, 0.865260124206543, 0.8595351576805115, 0.8430991172790527, 0.8404079079627991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0317330360412598})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7248955965042114})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6976903676986694})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.804752767086029})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7813959121704102})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9168870449066162})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8944, 'crossentropy': 0.60658525390625}
store['active_learning_steps'][29]['acquisition']={'indices': [3370, 51337, 14715, 24587, 33222], 'labels': [4, 4, 4, 8, 5], 'scores': [0.9210537075996399, 0.9125049114227295, 0.8893154263496399, 0.8597343564033508, 0.8518989086151123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0138065814971924})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6695421934127808})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7595970630645752})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8171656727790833})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7415904998779297})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.61182529296875}
store['active_learning_steps'][30]['acquisition']={'indices': [51464, 39305, 47278, 33057, 27898], 'labels': [0, 7, 5, 7, 2], 'scores': [0.8602278828620911, 0.8557986617088318, 0.8441089987754822, 0.8390310406684875, 0.8381412625312805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9816579818725586})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7166702151298523})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6769380569458008})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7107630968093872})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7646712064743042})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7205767035484314})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.56797421875}
store['active_learning_steps'][31]['acquisition']={'indices': [48323, 37403, 59390, 52319, 39487], 'labels': [2, 2, 2, 2, 2], 'scores': [0.9530657529830933, 0.9479461312294006, 0.9342395067214966, 0.8943389654159546, 0.8722807765007019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9369502067565918})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6663786768913269})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7218754291534424})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6836305260658264})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7541904449462891})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8943, 'crossentropy': 0.61368408203125}
store['active_learning_steps'][32]['acquisition']={'indices': [57523, 13827, 39818, 55743, 6474], 'labels': [3, 3, 1, 3, 6], 'scores': [0.9001772403717041, 0.8341128826141357, 0.8286564946174622, 0.8203381896018982, 0.8150246143341064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0674128532409668})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6411880254745483})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7037162184715271})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6378756761550903})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7885584831237793})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7657116651535034})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7586196660995483})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.57870849609375}
store['active_learning_steps'][33]['acquisition']={'indices': [36884, 42121, 39480, 37758, 31664], 'labels': [2, 5, 9, 0, 3], 'scores': [1.0101675391197205, 0.9832949042320251, 0.9759671092033386, 0.9681100845336914, 0.9508270621299744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.114441990852356})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6873784065246582})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6266295909881592})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6919312477111816})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7545249462127686})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.737182080745697})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.54907861328125}
store['active_learning_steps'][34]['acquisition']={'indices': [4185, 11693, 35401, 51764, 36818], 'labels': [2, 3, 3, 5, 7], 'scores': [0.9076202511787415, 0.8894091844558716, 0.8613144755363464, 0.8606208562850952, 0.8486461043357849]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0733795166015625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.791141927242279})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7466573715209961})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7101180553436279})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7645068168640137})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8452491760253906})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7970892190933228})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.644417724609375}
store['active_learning_steps'][35]['acquisition']={'indices': [34328, 18501, 45069, 12043, 24457], 'labels': [8, 4, 4, 8, 8], 'scores': [1.0258722305297852, 1.0257667303085327, 0.9975172877311707, 0.9722001552581787, 0.9686220288276672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9533711075782776})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7334610223770142})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6429566144943237})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.655060887336731})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6749306917190552})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6149623394012451})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7080351114273071})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6825300455093384})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6967943906784058})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.536448974609375}
store['active_learning_steps'][36]['acquisition']={'indices': [41218, 46828, 37583, 5762, 53324], 'labels': [8, 9, -1, 2, 9], 'scores': [1.0753619074821472, 1.0420501232147217, 0.9988263249397278, 0.9859809875488281, 0.9840953350067139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9137480854988098})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6270120739936829})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6655197143554688})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6366024613380432})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6981601715087891})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.567503955078125}
store['active_learning_steps'][37]['acquisition']={'indices': [6466, 55128, 40654, 22083, 12514], 'labels': [2, 8, 5, 2, 2], 'scores': [0.7853697538375854, 0.7786890864372253, 0.7636280059814453, 0.761914849281311, 0.7332829236984253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0730135440826416})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6882771253585815})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6268094778060913})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5577192902565002})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7151679396629333})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7160940170288086})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7533636689186096})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.516176171875}
store['active_learning_steps'][38]['acquisition']={'indices': [43745, 17377, 44661, 34090, 12277], 'labels': [8, 9, 1, 9, 9], 'scores': [1.0611544847488403, 0.9662331342697144, 0.9641680121421814, 0.9233264923095703, 0.9144473075866699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0136029720306396})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5568019151687622})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5191431641578674})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6029585003852844})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5859981179237366})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5455633401870728})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.482721142578125}
store['active_learning_steps'][39]['acquisition']={'indices': [50461, 11600, 37347, 17817, 18720], 'labels': [7, 2, 2, 9, 7], 'scores': [0.8957493901252747, 0.8857830762863159, 0.8824713230133057, 0.8478597402572632, 0.8462949991226196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9682020545005798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5947604179382324})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6349601745605469})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6630711555480957})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.672682523727417})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.56184716796875}
store['active_learning_steps'][40]['acquisition']={'indices': [8812, 12748, 51415, 25823, 58560], 'labels': [0, 0, 0, 0, 0], 'scores': [0.7785249948501587, 0.7727213501930237, 0.7693912386894226, 0.7527613639831543, 0.7516536116600037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1082773208618164})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5804548263549805})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5525349378585815})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6010468006134033})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6706739664077759})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6211017370223999})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.479408837890625}
store['active_learning_steps'][41]['acquisition']={'indices': [44754, 52938, 49890, 31794, 52086], 'labels': [-1, 2, 5, 2, 5], 'scores': [0.8691544532775879, 0.8618612885475159, 0.854933500289917, 0.8310865759849548, 0.8286727070808411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.046393632888794})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5824164152145386})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5316588878631592})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5483521223068237})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6356137990951538})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6075699329376221})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.50714677734375}
store['active_learning_steps'][42]['acquisition']={'indices': [47987, 31065, 10992, 13455, 46795], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8900161385536194, 0.8703655004501343, 0.8515979647636414, 0.8462121486663818, 0.8381265997886658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0891811847686768})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6132708191871643})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5798856019973755})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5617424845695496})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6038116216659546})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5917317867279053})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5608700513839722})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7196387648582458})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.681185245513916})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6989858746528625})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.50579521484375}
store['active_learning_steps'][43]['acquisition']={'indices': [26062, 54950, 10500, 43034, 38275], 'labels': [5, 8, 1, 9, 2], 'scores': [1.0306049585342407, 1.0040817856788635, 1.0023016929626465, 0.9997479915618896, 0.9707291722297668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9535781741142273})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5462764501571655})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5275796055793762})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47431689500808716})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5396144390106201})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5995510220527649})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5827274322509766})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.462435205078125}
store['active_learning_steps'][44]['acquisition']={'indices': [33812, 59314, 17382, 9608, 16836], 'labels': [6, 9, 6, 8, 7], 'scores': [1.0996384024620056, 0.9697725772857666, 0.965648889541626, 0.9084593057632446, 0.9035545587539673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9486247301101685})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5768578052520752})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5167603492736816})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5413122773170471})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5868525505065918})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6013411283493042})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.45032763671875}
store['active_learning_steps'][45]['acquisition']={'indices': [4822, 1239, 32776, 28392, 22717], 'labels': [4, 8, 4, 3, 3], 'scores': [0.8630672693252563, 0.8319411277770996, 0.8180968761444092, 0.8062101602554321, 0.8046315908432007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0231114625930786})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6147847175598145})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5056263208389282})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.528790295124054})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5491940975189209})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5501389503479004})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.452842236328125}
store['active_learning_steps'][46]['acquisition']={'indices': [45954, 32276, 18042, 14558, 24424], 'labels': [8, 3, 0, 3, 1], 'scores': [0.8736443519592285, 0.8209235668182373, 0.8186155557632446, 0.8167816400527954, 0.7969470024108887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0869560241699219})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6004005670547485})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5067384839057922})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.584136962890625})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5924214124679565})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5940893292427063})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.460710498046875}
store['active_learning_steps'][47]['acquisition']={'indices': [28362, 49616, 48384, 49656, 51759], 'labels': [7, 7, 9, 9, 3], 'scores': [0.7918736934661865, 0.787734866142273, 0.7683555483818054, 0.7569760084152222, 0.7473487854003906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.127089500427246})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6907747387886047})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5517803430557251})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5450976490974426})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6014418601989746})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6291627883911133})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5788323283195496})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.477216259765625}
store['active_learning_steps'][48]['acquisition']={'indices': [27429, 18193, 12663, 5129, 59294], 'labels': [0, -1, 8, 2, 8], 'scores': [0.8753881454467773, 0.8730950355529785, 0.8323176503181458, 0.8320562243461609, 0.8318453431129456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2817875146865845})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6497231721878052})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5661129951477051})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5244662761688232})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5079024434089661})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5098369121551514})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5413857698440552})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.591748833656311})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.45183564453125}
store['active_learning_steps'][49]['acquisition']={'indices': [23086, 39668, 8932, 46368, 48102], 'labels': [8, 8, 0, 8, 7], 'scores': [0.9814023971557617, 0.9473810791969299, 0.9355104565620422, 0.9338510036468506, 0.9329023361206055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.157920479774475})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7132212519645691})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.546438992023468})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5529968738555908})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5802429914474487})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5119180679321289})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5746533870697021})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5799312591552734})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.504844605922699})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.55912184715271})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6952368021011353})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6576988697052002})
store['active_learning_steps'][50]['training']['best_epoch']=9
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.935, 'crossentropy': 0.4718294921875}
store['active_learning_steps'][50]['acquisition']={'indices': [1674, 51863, 17540, 19188, 50789], 'labels': [9, 9, 1, 1, 1], 'scores': [1.1143602132797241, 1.0835898518562317, 1.067278265953064, 1.0571602582931519, 1.0397536754608154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1893413066864014})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6683216094970703})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.617290735244751})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.551460325717926})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48867619037628174})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5525748133659363})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5731732845306396})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5700187683105469})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.422412646484375}
store['active_learning_steps'][51]['acquisition']={'indices': [37720, 16756, 20328, 28512, 43206], 'labels': [8, 7, 8, 5, 5], 'scores': [0.9692069888114929, 0.9278391003608704, 0.9262281060218811, 0.9017427563667297, 0.8979568481445312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1949222087860107})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6441331505775452})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5007848143577576})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6157705783843994})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5690897703170776})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5955369472503662})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.45377265625}
store['active_learning_steps'][52]['acquisition']={'indices': [21174, 22480, 50930, 48706, 49537], 'labels': [2, 4, 0, 6, 2], 'scores': [0.784417986869812, 0.7632898092269897, 0.7509247064590454, 0.7476352453231812, 0.7476223111152649]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0350773334503174})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5841972231864929})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5059185028076172})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4860071539878845})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5084407329559326})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5272572040557861})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5033479928970337})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9457, 'crossentropy': 0.4044382568359375}
store['active_learning_steps'][53]['acquisition']={'indices': [38389, 32880, 1075, 38920, 20050], 'labels': [7, 0, 7, 7, 9], 'scores': [0.9122530221939087, 0.9108965992927551, 0.8976699709892273, 0.8866865634918213, 0.8814600110054016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2171053886413574})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6709011793136597})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5151367783546448})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5044207572937012})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49623754620552063})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5233977437019348})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5049575567245483})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5313199758529663})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.467446240234375}
store['active_learning_steps'][54]['acquisition']={'indices': [1642, 12211, 966, 35864, 55947], 'labels': [6, 3, 3, 5, 3], 'scores': [0.946253776550293, 0.940071702003479, 0.9293556809425354, 0.9236499667167664, 0.9221280813217163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1897363662719727})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7501058578491211})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5988456010818481})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5218403339385986})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5042188167572021})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49453991651535034})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5436785221099854})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6070404052734375})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5441440343856812})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9455, 'crossentropy': 0.420842041015625}
store['active_learning_steps'][55]['acquisition']={'indices': [43256, 45903, 2803, 47587, 15848], 'labels': [3, 3, 3, 3, 3], 'scores': [1.0555680990219116, 1.003700315952301, 0.9828760623931885, 0.9637436866760254, 0.957861065864563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0640389919281006})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6204608678817749})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5215688347816467})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47004300355911255})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4725704789161682})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44640854001045227})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.464996337890625})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5054433345794678})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5137910842895508})
store['active_learning_steps'][56]['training']['best_epoch']=6
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.373390087890625}
store['active_learning_steps'][56]['acquisition']={'indices': [42428, 7949, 22531, 59783, 45602], 'labels': [5, -1, 4, 1, 5], 'scores': [1.006345272064209, 0.9509615898132324, 0.9440101385116577, 0.9356799721717834, 0.930558979511261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2975528240203857})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6550986766815186})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47126221656799316})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47769099473953247})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4565114974975586})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4912756681442261})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4667913615703583})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49365919828414917})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.40562265625}
store['active_learning_steps'][57]['acquisition']={'indices': [59280, 20663, 50916, 15106, 22824], 'labels': [8, 6, 4, 7, 9], 'scores': [0.9655023217201233, 0.9293015003204346, 0.9136781096458435, 0.9028509259223938, 0.8907219171524048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.141871452331543})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6644492149353027})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5164295434951782})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4704805612564087})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47775474190711975})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4715161919593811})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48923057317733765})
store['active_learning_steps'][58]['training']['best_epoch']=4
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9423, 'crossentropy': 0.4066853515625}
store['active_learning_steps'][58]['acquisition']={'indices': [8459, 9687, 42085, 14385, 262], 'labels': [5, 0, 5, 8, 2], 'scores': [0.9308604598045349, 0.8763434886932373, 0.8746045827865601, 0.8634041547775269, 0.8554350733757019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.155329942703247})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6546421647071838})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5368527173995972})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4865848422050476})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49844861030578613})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5220184922218323})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4991433024406433})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9448, 'crossentropy': 0.4195857421875}
store['active_learning_steps'][59]['acquisition']={'indices': [25332, 33364, 34829, 16909, 15855], 'labels': [2, 2, 5, 2, 5], 'scores': [0.8707483410835266, 0.8688802123069763, 0.8627834320068359, 0.8603472709655762, 0.8484041690826416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.14921236038208})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.67061448097229})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5243992805480957})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48987340927124023})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45607370138168335})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4814392924308777})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4866144061088562})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49202486872673035})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9479, 'crossentropy': 0.3796805419921875}
store['active_learning_steps'][60]['acquisition']={'indices': [36072, 21601, 29002, 19495, 12984], 'labels': [2, 1, 7, 3, 8], 'scores': [0.9300575256347656, 0.8931736946105957, 0.8589981198310852, 0.8251345157623291, 0.8165427446365356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0663397312164307})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6549941301345825})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49756067991256714})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4636504650115967})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44522786140441895})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45235729217529297})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4186092019081116})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44039207696914673})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5168861150741577})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.427038311958313})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9549, 'crossentropy': 0.3635520751953125}
store['active_learning_steps'][61]['acquisition']={'indices': [13942, 20037, 38974, 4153, 41464], 'labels': [4, 8, 1, 2, 8], 'scores': [1.0396651029586792, 1.0395155549049377, 1.0370815992355347, 1.0342273116111755, 1.0222626328468323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2152729034423828})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6258257031440735})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5206406712532043})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.458553671836853})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4406607151031494})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4730650782585144})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4555450677871704})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45486029982566833})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.3787326904296875}
store['active_learning_steps'][62]['acquisition']={'indices': [33892, 7949, 41772, 35406, 9557], 'labels': [5, -1, 5, 5, 8], 'scores': [0.897344708442688, 0.8970255851745605, 0.8686008453369141, 0.8669770956039429, 0.8430532217025757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.257171392440796})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6368841528892517})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4762517809867859})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44906753301620483})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4579949975013733})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4397233724594116})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45861536264419556})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5612528324127197})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.489599347114563})
store['active_learning_steps'][63]['training']['best_epoch']=6
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.3748599365234375}
store['active_learning_steps'][63]['acquisition']={'indices': [14305, 5679, 37583, 670, 46126], 'labels': [8, 3, -1, 3, 3], 'scores': [1.0205891132354736, 1.0050013661384583, 0.9573604464530945, 0.9452400207519531, 0.9433218240737915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3063907623291016})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.616480827331543})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4535379409790039})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3976415991783142})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4303683638572693})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4554328918457031})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49065497517585754})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.37035791015625}
store['active_learning_steps'][64]['acquisition']={'indices': [4955, 18324, 53867, 50369, 1518], 'labels': [2, 0, 4, 3, 9], 'scores': [0.803318440914154, 0.7947887778282166, 0.7871484160423279, 0.7826142311096191, 0.7718246579170227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2586266994476318})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6848326921463013})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.50489741563797})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4897860288619995})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4700526297092438})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4279365539550781})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44513654708862305})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4267837405204773})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43162280321121216})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4136204719543457})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4778428077697754})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47218775749206543})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.434624582529068})
store['active_learning_steps'][65]['training']['best_epoch']=10
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.380572607421875}
store['active_learning_steps'][65]['acquisition']={'indices': [20859, 45062, 27829, 59720, 7719], 'labels': [8, 9, 0, 2, 2], 'scores': [1.1321504712104797, 1.0386244058609009, 1.0385308265686035, 1.0357755422592163, 1.0266914367675781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3659913539886475})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6959881782531738})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5335032939910889})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4779084622859955})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43358534574508667})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4600929617881775})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.478667676448822})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4260045289993286})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4161872863769531})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47542741894721985})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4510341286659241})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4745112657546997})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9557, 'crossentropy': 0.3568987060546875}
store['active_learning_steps'][66]['acquisition']={'indices': [27740, 15629, 45550, 52889, 43950], 'labels': [8, 8, -1, -1, 9], 'scores': [1.0557178258895874, 1.0547425150871277, 1.0166893601417542, 1.0156375765800476, 1.0067241787910461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1953685283660889})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6240514516830444})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48082900047302246})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38232356309890747})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4011121988296509})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3699846863746643})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40066057443618774})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4216163754463196})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39780664443969727})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3577755126953125}
store['active_learning_steps'][67]['acquisition']={'indices': [50317, 52889, 27503, 47549, 46441], 'labels': [3, -1, 2, 8, 6], 'scores': [0.9253505766391754, 0.883305013179779, 0.8779266476631165, 0.8776898384094238, 0.8761088848114014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1928883790969849})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6388657689094543})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49457111954689026})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4143918752670288})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4252614974975586})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4492987394332886})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44302666187286377})
store['active_learning_steps'][68]['training']['best_epoch']=4
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9572, 'crossentropy': 0.375198583984375}
store['active_learning_steps'][68]['acquisition']={'indices': [41453, 36363, 45666, 7984, 35326], 'labels': [3, 6, 1, 4, 5], 'scores': [0.7852299213409424, 0.7817866206169128, 0.7771840691566467, 0.7757728695869446, 0.7730364203453064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2227387428283691})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6141760349273682})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45096075534820557})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38844990730285645})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37803924083709717})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41443902254104614})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4002262353897095})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4123171269893646})
store['active_learning_steps'][69]['training']['best_epoch']=5
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.3427654296875}
store['active_learning_steps'][69]['acquisition']={'indices': [7851, 27358, 32289, 57665, 20363], 'labels': [8, 8, 7, 8, 8], 'scores': [0.877214252948761, 0.857723593711853, 0.8571851849555969, 0.855963408946991, 0.8520538806915283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1659396886825562})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6008024215698242})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4549524188041687})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.37102776765823364})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42349135875701904})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40387845039367676})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3804279565811157})
store['active_learning_steps'][70]['training']['best_epoch']=4
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.35859306640625}
store['active_learning_steps'][70]['acquisition']={'indices': [1160, 52889, 45761, 21426, 17603], 'labels': [4, -1, 4, 6, 0], 'scores': [0.7822144627571106, 0.7734948396682739, 0.7732664942741394, 0.7551162838935852, 0.7543699741363525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3635756969451904})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7287158370018005})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6058861017227173})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49328917264938354})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.45236313343048096})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41856905817985535})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3855157494544983})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3859007656574249})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40613672137260437})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.436947226524353})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.3728572509765625}
store['active_learning_steps'][71]['acquisition']={'indices': [58832, 57742, 29530, 9147, 32519], 'labels': [3, 6, 4, 4, 5], 'scores': [0.9463339447975159, 0.931119978427887, 0.9177717566490173, 0.9103937149047852, 0.9060632586479187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2006627321243286})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6022839546203613})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.460548996925354})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3519935607910156})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3871968388557434})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39014172554016113})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37568384408950806})
store['active_learning_steps'][72]['training']['best_epoch']=4
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.360064697265625}
store['active_learning_steps'][72]['acquisition']={'indices': [29511, 54858, 49192, 34406, 31557], 'labels': [-1, 3, 2, 4, -1], 'scores': [0.8891382813453674, 0.8670306205749512, 0.8510637879371643, 0.8449822068214417, 0.8352164030075073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3061802387237549})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6681703329086304})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5269681215286255})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4048536419868469})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3970198631286621})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40501365065574646})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.374865859746933})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36725330352783203})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3578057885169983})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37707287073135376})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40153127908706665})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3855676054954529})
store['active_learning_steps'][73]['training']['best_epoch']=9
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.3371100830078125}
store['active_learning_steps'][73]['acquisition']={'indices': [37583, 18487, 48006, 34133, 13969], 'labels': [-1, 4, 6, -1, 3], 'scores': [1.0511914491653442, 1.0233361721038818, 1.0086902976036072, 0.9962663054466248, 0.9937180876731873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.22926664352417})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6375806331634521})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5009310245513916})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4278963804244995})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4244343340396881})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3647710680961609})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3675616383552551})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3662770986557007})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41921475529670715})
store['active_learning_steps'][74]['training']['best_epoch']=6
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9616, 'crossentropy': 0.335836083984375}
store['active_learning_steps'][74]['acquisition']={'indices': [4741, 7949, 3694, 52169, 53054], 'labels': [6, -1, -1, 2, -1], 'scores': [1.0170912146568298, 1.0110933780670166, 0.9847238659858704, 0.9516186714172363, 0.9335394501686096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.242250680923462})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6567721962928772})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47835689783096313})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42808210849761963})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4018990993499756})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39836305379867554})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41317182779312134})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.366288959980011})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3842402696609497})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3410613536834717})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41121768951416016})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35133540630340576})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3916437029838562})
store['active_learning_steps'][75]['training']['best_epoch']=10
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.332667041015625}
store['active_learning_steps'][75]['acquisition']={'indices': [32573, 5295, 5163, 50714, 25624], 'labels': [8, 4, 8, 8, -1], 'scores': [1.0927404761314392, 1.0169116258621216, 0.9938709139823914, 0.9893079400062561, 0.9748953580856323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1572678089141846})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6625548601150513})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.47506600618362427})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.4237343668937683})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3735816478729248})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3241250216960907})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32496464252471924})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33183592557907104})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31474974751472473})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31656312942504883})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3379163146018982})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32848918437957764})
store['active_learning_steps'][76]['training']['best_epoch']=9
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.3232626708984375}
store['active_learning_steps'][76]['acquisition']={'indices': [7949, 43212, 41426, 22139, 41196], 'labels': [-1, 5, 4, 2, 9], 'scores': [0.9769482612609863, 0.9727413654327393, 0.958156168460846, 0.9566620588302612, 0.9393057227134705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.245448112487793})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6001286506652832})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4796258807182312})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41175609827041626})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3741235136985779})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3408355712890625})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3542768955230713})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3092595338821411})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3549087941646576})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36258983612060547})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3418320417404175})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.3223857177734375}
store['active_learning_steps'][77]['acquisition']={'indices': [59681, 43575, 13259, 49515, 11767], 'labels': [0, 2, 1, 2, 4], 'scores': [0.9814490079879761, 0.946499228477478, 0.9073303937911987, 0.8956738710403442, 0.8949050903320312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.419661283493042})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7282549738883972})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47971081733703613})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38195160031318665})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34998348355293274})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37308162450790405})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3856881260871887})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38164299726486206})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.353679443359375}
store['active_learning_steps'][78]['acquisition']={'indices': [29376, 28536, 55244, 50403, 6309], 'labels': [-1, 3, 7, -1, 3], 'scores': [0.8905057907104492, 0.8417277932167053, 0.8397064208984375, 0.833381712436676, 0.832760214805603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3981642723083496})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.7239270210266113})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5036840438842773})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37925267219543457})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3572559058666229})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37107399106025696})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35182908177375793})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3543197512626648})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3577563464641571})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31929582357406616})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35237693786621094})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3370589017868042})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36839428544044495})
store['active_learning_steps'][79]['training']['best_epoch']=10
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.311593505859375}
store['active_learning_steps'][79]['acquisition']={'indices': [5062, 18307, 2934, 53054, 32784], 'labels': [9, -1, 9, -1, 8], 'scores': [1.027436375617981, 1.0079962611198425, 1.0066556930541992, 0.9995259046554565, 0.989712119102478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2897316217422485})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.7291781306266785})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45469123125076294})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38835492730140686})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39689743518829346})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3746759593486786})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3436967134475708})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3401840031147003})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3543768525123596})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3501899838447571})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33547478914260864})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32965970039367676})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3250551223754883})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35303807258605957})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3550236225128174})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3690633773803711})
store['active_learning_steps'][80]['training']['best_epoch']=13
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.3099808837890625}
store['active_learning_steps'][80]['acquisition']={'indices': [9677, 31738, 53872, 55268, 17055], 'labels': [0, 8, 8, 8, 8], 'scores': [1.1416293382644653, 1.1287153959274292, 1.0834957957267761, 1.0726786851882935, 1.0711811780929565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3564233779907227})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6257953643798828})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4646603465080261})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3537488579750061})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3517661988735199})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3559737503528595})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38494932651519775})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3383265435695648})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3285723328590393})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38422060012817383})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3576417565345764})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33296674489974976})
store['active_learning_steps'][81]['training']['best_epoch']=9
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.292420263671875}
store['active_learning_steps'][81]['acquisition']={'indices': [36337, 49543, 53919, 7949, 46088], 'labels': [3, 8, -1, -1, 6], 'scores': [1.0120680332183838, 0.9567641019821167, 0.948503315448761, 0.9481600522994995, 0.94605952501297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.4676190614700317})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8895630240440369})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5491600036621094})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39503800868988037})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3556625247001648})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3263412117958069})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35109320282936096})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.357312947511673})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3241557478904724})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36153221130371094})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3660075068473816})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3160794675350189})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36771446466445923})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3707008957862854})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3376917839050293})
store['active_learning_steps'][82]['training']['best_epoch']=12
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.3368829833984375}
store['active_learning_steps'][82]['acquisition']={'indices': [21700, 2574, 9340, 54885, 59726], 'labels': [7, -1, 5, 6, -1], 'scores': [1.0513079166412354, 1.0317075848579407, 1.014693707227707, 0.9855013489723206, 0.9809868931770325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3219149112701416})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6097973585128784})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.481478750705719})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4376160800457001})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3649606704711914})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3422166705131531})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3171611726284027})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3255379796028137})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31477558612823486})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36860865354537964})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3819534182548523})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34226882457733154})
store['active_learning_steps'][83]['training']['best_epoch']=9
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9651, 'crossentropy': 0.30208828125}
store['active_learning_steps'][83]['acquisition']={'indices': [10195, 57575, 29672, 43811, 30897], 'labels': [0, 0, 9, 0, 3], 'scores': [1.018060028553009, 1.0017595291137695, 0.9534741640090942, 0.9516693353652954, 0.9512112140655518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3113491535186768})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7229610681533813})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5473690629005432})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4121842384338379})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34572577476501465})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38761618733406067})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.353663831949234})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3542329668998718})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9559, 'crossentropy': 0.3600015625}
store['active_learning_steps'][84]['acquisition']={'indices': [54316, 16731, 31252, 40382, 41802], 'labels': [6, -1, 5, 3, 2], 'scores': [0.7912382483482361, 0.7665188908576965, 0.7627826929092407, 0.7559736967086792, 0.7407262921333313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2969787120819092})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6932971477508545})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.45582228899002075})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.44109654426574707})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.364509642124176})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3466761112213135})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.32766157388687134})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.307147353887558})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27999112010002136})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3005567789077759})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3314248323440552})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3045273423194885})
store['active_learning_steps'][85]['training']['best_epoch']=9
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2843076416015625}
store['active_learning_steps'][85]['acquisition']={'indices': [52889, 40378, 57728, 20641, 55778], 'labels': [-1, -1, 9, 9, -1], 'scores': [1.0161283612251282, 0.9927811622619629, 0.9152219891548157, 0.9101113677024841, 0.9053598642349243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4263533353805542})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6945483684539795})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4843277633190155})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3702894151210785})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33428889513015747})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3289807438850403})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32564011216163635})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28943711519241333})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30438077449798584})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33129459619522095})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.33307313919067383})
store['active_learning_steps'][86]['training']['best_epoch']=8
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2967503173828125}
store['active_learning_steps'][86]['acquisition']={'indices': [52889, 3251, 59289, 7638, 36417], 'labels': [-1, 8, 1, 8, 6], 'scores': [0.9492967128753662, 0.9479284286499023, 0.9342861175537109, 0.9250698089599609, 0.9151245951652527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.3023700714111328})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7070965766906738})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.5388495922088623})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.43040308356285095})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3719537854194641})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3369741141796112})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3229944109916687})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32686737179756165})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3129924535751343})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3627985715866089})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.396433025598526})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3246218264102936})
store['active_learning_steps'][87]['training']['best_epoch']=9
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.319855712890625}
store['active_learning_steps'][87]['acquisition']={'indices': [18193, 39208, 56014, 30322, 53736], 'labels': [-1, 5, 5, 8, 9], 'scores': [1.0420840978622437, 0.9638471007347107, 0.9573273658752441, 0.9484915733337402, 0.9416961073875427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.344029426574707})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.7564876079559326})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4684249758720398})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37000522017478943})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3704473078250885})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34145697951316833})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.32998228073120117})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30823588371276855})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3108365535736084})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2990823984146118})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3332275152206421})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2975445091724396})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.352999746799469})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3352370262145996})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3392428159713745})
store['active_learning_steps'][88]['training']['best_epoch']=12
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.298798388671875}
store['active_learning_steps'][88]['acquisition']={'indices': [3694, 31591, 20832, 31882, 8643], 'labels': [-1, 8, 2, -1, -1], 'scores': [1.0517290234565735, 1.049017310142517, 1.005714237689972, 0.9938417077064514, 0.9932369589805603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.501384973526001})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.7917261123657227})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.535521388053894})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.37988707423210144})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.350736528635025})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3618728816509247})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3489033579826355})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3458020091056824})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.35752296447753906})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33480769395828247})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.398038387298584})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.389710009098053})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38825559616088867})
store['active_learning_steps'][89]['training']['best_epoch']=10
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.341246533203125}
store['active_learning_steps'][89]['acquisition']={'indices': [48824, 16022, 32419, 29360, 52914], 'labels': [8, 8, 4, 8, 5], 'scores': [0.9916810393333435, 0.9852677583694458, 0.9745129942893982, 0.9702463150024414, 0.9656167030334473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.3043758869171143})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7330687046051025})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.5038318634033203})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.39984971284866333})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3849727511405945})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.35028672218322754})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3669503331184387})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3199204206466675})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3165624737739563})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33646631240844727})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.35517579317092896})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34468334913253784})
store['active_learning_steps'][90]['training']['best_epoch']=9
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.29207568359375}
store['active_learning_steps'][90]['acquisition']={'indices': [29511, 2591, 36867, 59731, 9117], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.0256248116493225, 0.997001051902771, 0.979423999786377, 0.9719951152801514, 0.9704412221908569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.300144076347351})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5884116888046265})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4095437526702881})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3264809548854828})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35081809759140015})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32392168045043945})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2861173450946808})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3105959892272949})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33799034357070923})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33274662494659424})
store['active_learning_steps'][91]['training']['best_epoch']=7
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.29073671875}
store['active_learning_steps'][91]['acquisition']={'indices': [10184, 28652, 54097, 13195, 58094], 'labels': [9, 4, 7, -1, 7], 'scores': [0.9180464446544647, 0.9121161103248596, 0.9008186459541321, 0.8958454132080078, 0.8893404006958008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3601279258728027})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.7296990156173706})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.43489864468574524})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37820976972579956})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3330637216567993})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32898980379104614})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29684603214263916})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31845563650131226})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.311725378036499})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32830697298049927})
store['active_learning_steps'][92]['training']['best_epoch']=7
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2920211181640625}
store['active_learning_steps'][92]['acquisition']={'indices': [13156, 33426, 6418, 51394, 29376], 'labels': [2, 4, 5, 8, -1], 'scores': [0.9434611201286316, 0.9176887571811676, 0.8993566036224365, 0.8906291127204895, 0.8887599110603333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3189611434936523})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6649638414382935})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5115170478820801})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.372524619102478})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3642912805080414})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3407330811023712})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3287326693534851})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3321020007133484})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30105143785476685})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3346360921859741})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32015031576156616})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3131767511367798})
store['active_learning_steps'][93]['training']['best_epoch']=9
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.310009228515625}
store['active_learning_steps'][93]['acquisition']={'indices': [36990, 19702, 53054, 18307, 46734], 'labels': [-1, 5, -1, -1, 4], 'scores': [0.9643943309783936, 0.9343831539154053, 0.9185462594032288, 0.9090902805328369, 0.8964496850967407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.4137150049209595})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.746729850769043})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4954747259616852})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4349369406700134})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3360322117805481})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32234007120132446})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3340833783149719})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3084559440612793})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3155277967453003})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3404553532600403})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31467628479003906})
store['active_learning_steps'][94]['training']['best_epoch']=8
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.294876123046875}
store['active_learning_steps'][94]['acquisition']={'indices': [22098, 14210, 22193, 15779, 49282], 'labels': [-1, -1, 5, 0, 2], 'scores': [0.9165002703666687, 0.9060456156730652, 0.8908118605613708, 0.8829349875450134, 0.8766695857048035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.286581039428711})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7635065913200378})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4954894781112671})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4100390672683716})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31557756662368774})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3147844672203064})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3591112196445465})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3023737072944641})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32813596725463867})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33165860176086426})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31057149171829224})
store['active_learning_steps'][95]['training']['best_epoch']=8
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.30281083984375}
store['active_learning_steps'][95]['acquisition']={'indices': [22364, 40066, 47626, 16731, 46547], 'labels': [0, 4, -1, -1, -1], 'scores': [0.9762469530105591, 0.9593169689178467, 0.8711079359054565, 0.866985023021698, 0.8616914749145508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.5221378803253174})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.7692232728004456})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5108013153076172})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.4086800813674927})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.330223947763443})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30905967950820923})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3325214385986328})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3266465663909912})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3261399269104004})
store['active_learning_steps'][96]['training']['best_epoch']=6
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.314178564453125}
store['active_learning_steps'][96]['acquisition']={'indices': [29320, 6440, 44328, 470, 2862], 'labels': [1, 3, 9, 1, 6], 'scores': [0.9009003043174744, 0.8570922017097473, 0.8383148908615112, 0.8382870554924011, 0.8285775184631348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3674829006195068})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.752236008644104})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5423288941383362})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42273908853530884})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.34435397386550903})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32676875591278076})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.30152082443237305})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3391471803188324})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3029218912124634})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3264005482196808})
store['active_learning_steps'][97]['training']['best_epoch']=7
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.3048070068359375}
store['active_learning_steps'][97]['acquisition']={'indices': [41933, 38698, 1512, 39405, 24756], 'labels': [5, 5, 0, 5, -1], 'scores': [0.9312418699264526, 0.9272571206092834, 0.8815231323242188, 0.849061131477356, 0.8466591238975525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.526442050933838})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.8010249137878418})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5795552730560303})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4813683032989502})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4093688428401947})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3760853409767151})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3129503130912781})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36649221181869507})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3505648970603943})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33314311504364014})
store['active_learning_steps'][98]['training']['best_epoch']=7
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.314283935546875}
