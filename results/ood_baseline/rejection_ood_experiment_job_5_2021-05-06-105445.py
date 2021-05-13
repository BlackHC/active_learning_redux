store = {}
store['timestamp']=1620294885
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=5']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=5
store['worker_id']=5
store['num_workers']=40
store['config']={'seed': 6, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1609513759613037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.5409998893737793})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.603879928588867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8016676902770996})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6702, 'crossentropy': 1.979759765625}
store['active_learning_steps'][0]['acquisition']={'indices': [22675, 29361, 1724, 57578, 34847, 50052, 13305, 16959, 18971, 38256], 'labels': [3, 5, 2, 6, 0, 2, 5, 5, 6, 2], 'scores': [1.2031627297401428, 1.180902898311615, 1.1698349714279175, 1.1607902646064758, 1.153287947177887, 1.1471675038337708, 1.1446464657783508, 1.1438890099525452, 1.1323641538619995, 1.132097601890564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8968935012817383})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.352529525756836})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5976715087890625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.7167134284973145})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6986, 'crossentropy': 1.7560279296875}
store['active_learning_steps'][1]['acquisition']={'indices': [12275, 8479, 16692, 5409, 37313, 28512, 47707, 41539, 55643, 3494], 'labels': [8, 5, 5, 8, 5, 5, 5, 5, 5, 7], 'scores': [1.0764793157577515, 1.0684010982513428, 1.0571839213371277, 1.0556603074073792, 1.0479510426521301, 1.0433141589164734, 1.042275071144104, 1.0343221426010132, 1.031293272972107, 1.0296658277511597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.7590100765228271})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.441053867340088})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.524263858795166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.671905040740967})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7021, 'crossentropy': 1.61166494140625}
store['active_learning_steps'][2]['acquisition']={'indices': [39179, 12973, 4606, 58811, 31400, 33642, 23347, 5728, 12202, 20982], 'labels': [9, 4, 9, 2, 9, 9, 8, 3, 9, 9], 'scores': [1.0774558782577515, 1.0509734749794006, 1.0443960428237915, 1.040443480014801, 1.0385246276855469, 1.0384150743484497, 1.0378237962722778, 1.037516713142395, 1.0358100533485413, 1.0346000790596008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.666714072227478})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.7408814430236816})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.935948371887207})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.8882079124450684})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7228, 'crossentropy': 1.502555078125}
store['active_learning_steps'][3]['acquisition']={'indices': [41340, 49179, 58116, 8289, 46727, 9303, 39283, 13366, 36662, 9588], 'labels': [2, 2, 0, 0, 2, 3, 2, 0, 2, 7], 'scores': [0.9980176687240601, 0.9617519378662109, 0.943764865398407, 0.9383692741394043, 0.9311633110046387, 0.930567741394043, 0.9303697347640991, 0.929552435874939, 0.9292174577713013, 0.9242014288902283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8638560771942139})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.702854037284851})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.7549484968185425})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.011533260345459})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.199092149734497})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7639, 'crossentropy': 1.489009765625}
store['active_learning_steps'][4]['acquisition']={'indices': [19187, 25521, 40688, 51762, 36531, 483, 49992, 13119, 3870, 28924], 'labels': [7, 5, 5, 5, 7, 7, 5, 7, 5, 5], 'scores': [1.0281569361686707, 1.0061680674552917, 0.9909276366233826, 0.9802164435386658, 0.9749134182929993, 0.9722615480422974, 0.9713532328605652, 0.9708765745162964, 0.9700015783309937, 0.9677636623382568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.264749526977539})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.4410388469696045})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.765787124633789})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.750150442123413})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.765, 'crossentropy': 1.17917939453125}
store['active_learning_steps'][5]['acquisition']={'indices': [5740, 48356, 49060, 35267, 55513, 57245, 42515, 42671, 45753, 52006], 'labels': [9, 2, 6, 5, 5, 2, 8, 2, 5, 2], 'scores': [0.990803599357605, 0.9620121717453003, 0.9504956603050232, 0.9458303451538086, 0.9433783292770386, 0.9420056343078613, 0.9355836510658264, 0.9155024290084839, 0.9077420234680176, 0.9025821089744568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4500101804733276})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3355827331542969})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6741065979003906})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.5487353801727295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.706617832183838})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7654, 'crossentropy': 1.34218984375}
store['active_learning_steps'][6]['acquisition']={'indices': [14335, 11534, 12345, 35232, 40702, 33697, 22481, 24589, 35344, 35946], 'labels': [4, 7, 3, 8, 4, 2, 7, 8, 2, 4], 'scores': [1.0572611689567566, 1.0018786787986755, 0.9961331486701965, 0.9909995198249817, 0.9854332804679871, 0.9807275533676147, 0.97304767370224, 0.9660935401916504, 0.9653633832931519, 0.9644799828529358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.296858787536621})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3553968667984009})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2581732273101807})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.6661503314971924})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.6045758724212646})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.724916696548462})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8196, 'crossentropy': 1.0352650390625}
store['active_learning_steps'][7]['acquisition']={'indices': [2352, 36281, 44807, 1916, 5474, 20273, 17486, 48271, 8516, 40712], 'labels': [0, 7, 7, 0, 8, 7, 7, 7, 7, 7], 'scores': [1.1232060194015503, 1.1157752871513367, 1.0982083082199097, 1.082168161869049, 1.0740630626678467, 1.0687728822231293, 1.0663121342658997, 1.0636566281318665, 1.054624855518341, 1.0463416576385498]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9664922952651978})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9501050710678101})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0282059907913208})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2606704235076904})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.095725178718567})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8502, 'crossentropy': 0.83978857421875}
store['active_learning_steps'][8]['acquisition']={'indices': [53872, 29132, 4701, 36229, 51764, 54973, 14896, 3810, 40208, 50576], 'labels': [8, 8, 2, 2, 5, 2, 8, 3, 0, 2], 'scores': [0.9888502359390259, 0.9794067740440369, 0.978689432144165, 0.9654445648193359, 0.9184569120407104, 0.9171473383903503, 0.9155415296554565, 0.9097439646720886, 0.9068225026130676, 0.9061181545257568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0693589448928833})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9554777145385742})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0122873783111572})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.08859384059906})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0141040086746216})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 0.89019755859375}
store['active_learning_steps'][9]['acquisition']={'indices': [3070, 51544, 134, 11600, 19923, 55282, 29764, 14765, 25048, 12196], 'labels': [1, 1, 1, 2, 4, 4, 4, 3, 4, 2], 'scores': [0.9421905279159546, 0.9221211671829224, 0.9207196235656738, 0.9178599119186401, 0.91758131980896, 0.9167957901954651, 0.9167351126670837, 0.8964851498603821, 0.8827987909317017, 0.8818620443344116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9954043626785278})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9312285780906677})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9924746751785278})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8877137899398804})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0154091119766235})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1107542514801025})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9988363981246948})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8612, 'crossentropy': 0.815879296875}
store['active_learning_steps'][10]['acquisition']={'indices': [22824, 8691, 44277, 59919, 33369, 25269, 46433, 37305, 59781, 30047], 'labels': [9, 2, 1, 1, 1, 1, 1, 1, 1, 1], 'scores': [1.0876800417900085, 1.0696877837181091, 1.0349392294883728, 1.0244316458702087, 1.0141249895095825, 1.004361093044281, 0.9987057447433472, 0.9907184839248657, 0.9894567728042603, 0.9893166422843933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9080215692520142})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8093215823173523})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9154294729232788})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8468503952026367})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8755051493644714})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.7203638671875}
store['active_learning_steps'][11]['acquisition']={'indices': [9180, 57728, 581, 21012, 16628, 49493, 52697, 37696, 15949, 47132], 'labels': [3, 9, 3, 2, 9, 8, 3, 2, 5, 2], 'scores': [0.9723639488220215, 0.9609460234642029, 0.9479786157608032, 0.9326382875442505, 0.9287320971488953, 0.9244908690452576, 0.9205799698829651, 0.9155107140541077, 0.9128658771514893, 0.9068291187286377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8965839743614197})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6896073818206787})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6982157230377197})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7599955797195435})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8291251063346863})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9025, 'crossentropy': 0.608866064453125}
store['active_learning_steps'][12]['acquisition']={'indices': [3719, 13149, 58560, 14152, 21880, 32519, 11777, 55128, 14337, 59280], 'labels': [2, 7, 0, 7, 2, 5, 3, 8, 7, 8], 'scores': [0.8585936427116394, 0.8568401336669922, 0.8494763970375061, 0.8418663144111633, 0.8251381516456604, 0.81834477186203, 0.811319887638092, 0.8091115355491638, 0.8076381683349609, 0.7998943328857422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9736782312393188})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7922569513320923})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8270790576934814})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7901960611343384})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7373982071876526})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8317590355873108})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8849400281906128})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9276782870292664})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.700226904296875}
store['active_learning_steps'][13]['acquisition']={'indices': [12497, 12986, 12305, 1127, 42632, 43961, 49199, 43782, 41371, 52140], 'labels': [0, 5, 9, 7, 0, 0, 0, 3, 0, 4], 'scores': [1.1086747646331787, 1.091954231262207, 1.0861343145370483, 1.0850115418434143, 1.0823225378990173, 1.0538763999938965, 1.0535143613815308, 1.0455072522163391, 1.0398879647254944, 1.0340973138809204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9265986680984497})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6881887912750244})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6242794990539551})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6990756392478943})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7388463616371155})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7339355945587158})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.581662109375}
store['active_learning_steps'][14]['acquisition']={'indices': [31301, 50343, 36818, 27503, 13709, 31184, 11298, 54994, 1812, 17005], 'labels': [5, 6, 7, 2, 6, 9, 2, 6, 4, 1], 'scores': [1.062686800956726, 0.9780027866363525, 0.9656857848167419, 0.9510705769062042, 0.9467811584472656, 0.945685088634491, 0.9345328509807587, 0.9290291666984558, 0.9112712740898132, 0.9078506827354431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.949915885925293})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.681973934173584})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.69021075963974})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.696797251701355})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8015245199203491})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8749, 'crossentropy': 0.68142265625}
store['active_learning_steps'][15]['acquisition']={'indices': [47741, 20169, 25384, 18003, 28469, 19396, 20111, 26302, 13021, 54146], 'labels': [5, 4, 5, 2, 5, 5, 9, 9, 5, 9], 'scores': [0.8940601348876953, 0.8821531534194946, 0.8657776713371277, 0.8325214385986328, 0.8296160697937012, 0.8103983402252197, 0.8053237795829773, 0.8008264899253845, 0.8002049922943115, 0.7966395020484924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.133984923362732})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7428104877471924})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7509686350822449})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6867169141769409})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8333454132080078})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7747131586074829})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.802487313747406})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.622031201171875}
store['active_learning_steps'][16]['acquisition']={'indices': [34765, 29803, 13259, 39818, 22561, 15190, 36417, 24633, 34966, 19597], 'labels': [6, 6, 1, 1, 6, 6, 6, 2, 8, 9], 'scores': [1.0412143468856812, 1.025827169418335, 1.011948823928833, 1.0028493404388428, 1.000230073928833, 0.9962888956069946, 0.9750770330429077, 0.9710661172866821, 0.9703670144081116, 0.9540585279464722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9575684070587158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.589953601360321})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5821022987365723})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6461738348007202})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6217507123947144})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6278392672538757})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.5419939453125}
store['active_learning_steps'][17]['acquisition']={'indices': [56427, 5295, 53854, 47626, 41307, 52889, 32510, 45026, 34520, 5175], 'labels': [2, 4, 8, -1, 4, -1, 2, 8, 6, 4], 'scores': [1.0461132526397705, 0.9722446799278259, 0.933529794216156, 0.9117215871810913, 0.908447802066803, 0.8998814821243286, 0.8922439813613892, 0.8881999850273132, 0.8862482905387878, 0.88422030210495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0071319341659546})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7319884300231934})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6893048882484436})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6069067120552063})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.692657470703125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6767759919166565})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7197567224502563})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.56373935546875}
store['active_learning_steps'][18]['acquisition']={'indices': [29068, 18473, 9687, 30418, 57985, 45121, 2765, 31345, 42774, 25662], 'labels': [-1, 4, 0, 8, 4, 4, 0, 3, 4, 4], 'scores': [1.0167610049247742, 1.003641128540039, 0.9964255094528198, 0.9697695374488831, 0.9598990678787231, 0.9570169448852539, 0.954070508480072, 0.9498342871665955, 0.9454306960105896, 0.9421466588973999]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9334789514541626})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6259651184082031})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6179755926132202})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6286969780921936})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6860188245773315})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6413384675979614})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.904, 'crossentropy': 0.55218642578125}
store['active_learning_steps'][19]['acquisition']={'indices': [35326, 19586, 5684, 35498, 7949, 16756, 20050, 32850, 19618, 11643], 'labels': [5, 9, 6, 3, -1, 7, 9, 3, 8, 5], 'scores': [0.8736267685890198, 0.8521986603736877, 0.8429922461509705, 0.8413479924201965, 0.8333061933517456, 0.8252577185630798, 0.8244677186012268, 0.8157069087028503, 0.8115799427032471, 0.8115760087966919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0099842548370361})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6323644518852234})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6227155923843384})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6113926768302917})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6271503567695618})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.581079363822937})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6903021931648254})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6142178773880005})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7071030735969543})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.511148876953125}
store['active_learning_steps'][20]['acquisition']={'indices': [45069, 15134, 53693, 2803, 59314, 14394, 39429, 52889, 8207, 14279], 'labels': [4, 6, 4, 3, 9, 3, 2, -1, 4, 8], 'scores': [1.0662986636161804, 1.029943823814392, 1.0212980508804321, 1.010183036327362, 0.997969925403595, 0.9978336691856384, 0.9927619695663452, 0.9718749523162842, 0.9567715525627136, 0.9521945118904114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8850585222244263})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5675302743911743})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5092856287956238})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.517830491065979})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6003748774528503})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5261461138725281})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.45779921875}
store['active_learning_steps'][21]['acquisition']={'indices': [8867, 18962, 41933, 22316, 8761, 43745, 5308, 4153, 15899, 50370], 'labels': [8, 7, 5, 9, 8, 8, 7, 2, 9, 7], 'scores': [0.8586733937263489, 0.8540918231010437, 0.847480058670044, 0.8462408781051636, 0.8425849676132202, 0.8418349027633667, 0.8415694832801819, 0.8343120813369751, 0.8296266794204712, 0.8264526724815369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0903801918029785})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5843710899353027})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5780849456787109})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.565017580986023})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5371894836425781})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6061784029006958})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6330423355102539})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5621962547302246})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9315, 'crossentropy': 0.479031005859375}
store['active_learning_steps'][22]['acquisition']={'indices': [36984, 24479, 57300, 52392, 50317, 31794, 5315, 7596, 23027, 46126], 'labels': [5, 8, 3, 1, 3, 2, 3, 4, -1, 3], 'scores': [0.9838057160377502, 0.9776042699813843, 0.96640545129776, 0.9544659852981567, 0.9540627002716064, 0.9534348249435425, 0.9499068260192871, 0.94742351770401, 0.9431248903274536, 0.9304742217063904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0312223434448242})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5709654092788696})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.505540132522583})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5107173919677734})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4873528480529785})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49977535009384155})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5273743271827698})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5534915924072266})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.44623125}
store['active_learning_steps'][23]['acquisition']={'indices': [45972, 34304, 39561, 42415, 34328, 42384, 32047, 4822, 32573, 26358], 'labels': [2, 8, 2, 7, 8, 8, 9, 4, 8, 3], 'scores': [1.0120174884796143, 0.9972242116928101, 0.9327424764633179, 0.9054781198501587, 0.903178334236145, 0.9024086594581604, 0.901849091053009, 0.9014031887054443, 0.9002999663352966, 0.897869884967804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0395267009735107})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5970957279205322})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4788200259208679})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5073213577270508})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5200340747833252})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49593228101730347})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.46072490234375}
store['active_learning_steps'][24]['acquisition']={'indices': [33892, 3370, 52169, 28199, 9118, 53019, 14649, 33594, 52959, 8978], 'labels': [5, 4, 2, 3, 9, 2, 0, 3, 2, 2], 'scores': [0.8041849732398987, 0.7985770106315613, 0.7974386811256409, 0.7802816033363342, 0.7741694450378418, 0.7650989294052124, 0.7644012570381165, 0.7541854381561279, 0.7540185451507568, 0.7505291700363159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0776257514953613})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.673737645149231})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5513919591903687})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48337632417678833})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.557325005531311})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5735273361206055})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5407023429870605})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9392, 'crossentropy': 0.455871240234375}
store['active_learning_steps'][25]['acquisition']={'indices': [12984, 37118, 31090, 16834, 38698, 7638, 21058, 9633, 424, 3273], 'labels': [8, 3, 4, 5, 5, 8, 5, 9, 9, 8], 'scores': [0.9674623012542725, 0.9376256465911865, 0.8957469463348389, 0.8707494139671326, 0.867888867855072, 0.865405261516571, 0.8593252301216125, 0.8545893430709839, 0.8497256636619568, 0.84676194190979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0625712871551514})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5531978607177734})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5050269961357117})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5114843845367432})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4686785340309143})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49707740545272827})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49184465408325195})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5452417135238647})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.42678603515625}
store['active_learning_steps'][26]['acquisition']={'indices': [59468, 50233, 52889, 22083, 24424, 25803, 22743, 966, 36450, 50461], 'labels': [7, 7, -1, 2, 1, 0, 7, 3, 2, 7], 'scores': [0.9783737659454346, 0.930839329957962, 0.9259951114654541, 0.9183970093727112, 0.9152505397796631, 0.9139399528503418, 0.9035901427268982, 0.9023239016532898, 0.8862320780754089, 0.8853428959846497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.147903561592102})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5656893253326416})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4960815906524658})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4595264196395874})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4551042914390564})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45752549171447754})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4649287760257721})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49534276127815247})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9444, 'crossentropy': 0.414428271484375}
store['active_learning_steps'][27]['acquisition']={'indices': [12702, 30962, 19188, 1674, 3762, 19502, 32427, 20005, 59731, 37469], 'labels': [3, 3, 1, 9, 8, 2, 0, 6, 5, 2], 'scores': [0.950609028339386, 0.9424246549606323, 0.8976032137870789, 0.8869049549102783, 0.8843041062355042, 0.8787476420402527, 0.8527297973632812, 0.8470219969749451, 0.8396310210227966, 0.8380094170570374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1618685722351074})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5960602760314941})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5242719054222107})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48529940843582153})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4750516414642334})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4901949465274811})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44898688793182373})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4986576437950134})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5721302032470703})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5424132943153381})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.42038212890625}
store['active_learning_steps'][28]['acquisition']={'indices': [42703, 55778, 24462, 47949, 50736, 23027, 59378, 37583, 5974, 21923], 'labels': [0, -1, 2, 5, -1, -1, -1, -1, -1, -1], 'scores': [1.0846859216690063, 1.0545275211334229, 1.0356584787368774, 0.9960678219795227, 0.9811455011367798, 0.9797982573509216, 0.964139997959137, 0.9604222774505615, 0.955203115940094, 0.9548068642616272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2568950653076172})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6330982446670532})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4964998960494995})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4459080994129181})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4810858368873596})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4350777864456177})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4649922549724579})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46608877182006836})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45686888694763184})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9486, 'crossentropy': 0.398743017578125}
store['active_learning_steps'][29]['acquisition']={'indices': [32880, 17603, 52086, 42428, 13998, 33812, 57972, 4784, 19078, 30451], 'labels': [0, 0, 5, 5, 9, 6, 4, 7, -1, 8], 'scores': [1.04976487159729, 0.9883275628089905, 0.9567004442214966, 0.9363511800765991, 0.933279812335968, 0.9326719641685486, 0.9162436723709106, 0.9119739532470703, 0.9075459837913513, 0.8971938490867615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0592479705810547})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6508527994155884})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4587149918079376})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5078678131103516})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44736647605895996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4460466504096985})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.458906888961792})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43797624111175537})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4698610305786133})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49619239568710327})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.485068142414093})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.395830224609375}
store['active_learning_steps'][30]['acquisition']={'indices': [24740, 55244, 2782, 43181, 17958, 48024, 39090, 23958, 29851, 46975], 'labels': [8, 7, -1, -1, 9, -1, -1, -1, -1, -1], 'scores': [1.0313186645507812, 1.0189931988716125, 0.9910301566123962, 0.9903134107589722, 0.9877426624298096, 0.9831665754318237, 0.9825572967529297, 0.9745599627494812, 0.9740349650382996, 0.9737284183502197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2345232963562012})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6231322288513184})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5274016857147217})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47737374901771545})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4403979182243347})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4270196259021759})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5033918023109436})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4704504609107971})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47180622816085815})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.3947134033203125}
store['active_learning_steps'][31]['acquisition']={'indices': [37078, 57311, 58832, 16911, 8879, 14706, 36409, 49890, 37773, 37450], 'labels': [8, 5, 3, 3, 3, 8, 3, 5, 9, 4], 'scores': [1.0098246335983276, 0.9142472743988037, 0.9109032154083252, 0.8977644443511963, 0.8778930902481079, 0.872929036617279, 0.8679602146148682, 0.8659274578094482, 0.8584371209144592, 0.8581401109695435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.159130573272705})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5885238647460938})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5397164821624756})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4987340569496155})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5192779302597046})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4575750231742859})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49947458505630493})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5220993757247925})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5233180522918701})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9464, 'crossentropy': 0.411854736328125}
store['active_learning_steps'][32]['acquisition']={'indices': [4741, 52294, 45602, 42078, 20110, 47220, 27085, 19344, 10064, 36072], 'labels': [6, 0, 5, 4, 4, 6, 8, 7, 8, 2], 'scores': [1.0417664647102356, 0.9680675864219666, 0.9386035799980164, 0.9380768537521362, 0.9378899335861206, 0.937579333782196, 0.936459481716156, 0.9036475121974945, 0.9017229676246643, 0.895558774471283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2543396949768066})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6941789388656616})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5497146248817444})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.494699627161026})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4802860617637634})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46883130073547363})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4804729223251343})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5463244318962097})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45470696687698364})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5180648565292358})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5258816480636597})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5964400768280029})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.446682666015625}
store['active_learning_steps'][33]['acquisition']={'indices': [36704, 44753, 48916, 20172, 33150, 35178, 36196, 34406, 40169, 38974], 'labels': [2, 5, -1, 4, 8, 4, -1, 4, 4, 1], 'scores': [1.0788106322288513, 1.052478551864624, 1.0180306434631348, 1.0118820071220398, 1.0020182728767395, 0.994599461555481, 0.9915629625320435, 0.9837920963764191, 0.9820302724838257, 0.9773949384689331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2951006889343262})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6999624371528625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4961169958114624})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.454201340675354})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45561808347702026})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44559359550476074})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4419848322868347})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49299031496047974})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.49684637784957886})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.48009949922561646})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9486, 'crossentropy': 0.396851220703125}
store['active_learning_steps'][34]['acquisition']={'indices': [57523, 42437, 53736, 20820, 16836, 41537, 16528, 58064, 32108, 32668], 'labels': [3, 9, 9, 9, 7, 3, 7, 3, 4, 9], 'scores': [1.0276155471801758, 0.9892551898956299, 0.9644551277160645, 0.9598984122276306, 0.9494660496711731, 0.9456264972686768, 0.9193162322044373, 0.9106338024139404, 0.904414176940918, 0.901339590549469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.381023645401001})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7536696195602417})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5404945611953735})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4804893136024475})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42956963181495667})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4632319211959839})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47194916009902954})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45748987793922424})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.406583984375}
store['active_learning_steps'][35]['acquisition']={'indices': [16011, 48006, 7816, 55906, 48454, 18042, 32776, 47036, 33364, 56662], 'labels': [5, 6, 0, 2, 1, 0, 4, 2, 2, 0], 'scores': [0.8456149101257324, 0.833932101726532, 0.8223340511322021, 0.8190820217132568, 0.8084988594055176, 0.8026415705680847, 0.8007549047470093, 0.8001270294189453, 0.7972783446311951, 0.7948111295700073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2414429187774658})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7006492018699646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43336570262908936})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4234355092048645})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42257368564605713})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4277452230453491})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37610647082328796})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4277820885181427})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4170008897781372})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3922896981239319})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9537, 'crossentropy': 0.3562284423828125}
store['active_learning_steps'][36]['acquisition']={'indices': [1518, 34385, 28536, 6269, 8447, 4185, 11572, 18493, 32747, 20709], 'labels': [9, -1, 3, 3, 3, 2, 5, 1, 8, 8], 'scores': [0.9221216440200806, 0.8931095600128174, 0.8781765699386597, 0.8751068711280823, 0.8740150928497314, 0.8601678609848022, 0.8543787002563477, 0.8535502552986145, 0.8507286906242371, 0.8489624261856079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.198700189590454})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7124089598655701})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5395228862762451})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43446648120880127})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4421811103820801})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4180607199668884})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3662755489349365})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38356202840805054})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41326794028282166})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39726722240448})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.3520689453125}
store['active_learning_steps'][37]['acquisition']={'indices': [6574, 49910, 13969, 46368, 4646, 54858, 51180, 588, 16853, 47595], 'labels': [-1, 6, 3, 8, 2, 3, 7, 2, -1, 7], 'scores': [0.9400604367256165, 0.9202326536178589, 0.9110596776008606, 0.8917820453643799, 0.8763651251792908, 0.867631733417511, 0.8666321635246277, 0.857550173997879, 0.8552400469779968, 0.85489422082901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1990232467651367})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6842424869537354})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5565717220306396})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5160483121871948})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44365090131759644})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46832746267318726})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44194334745407104})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44877350330352783})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4836970865726471})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4559360146522522})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.372722412109375}
store['active_learning_steps'][38]['acquisition']={'indices': [33505, 21668, 26444, 24620, 36760, 14726, 56773, 5750, 8297, 17190], 'labels': [2, 2, 1, 9, 7, 9, 9, 6, 7, 9], 'scores': [0.9477458596229553, 0.9095566868782043, 0.9070165753364563, 0.9067537784576416, 0.8995997309684753, 0.8960918188095093, 0.8957476615905762, 0.8829042911529541, 0.8701502680778503, 0.8701249957084656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3223133087158203})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6707426905632019})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4576911926269531})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4188481271266937})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40749022364616394})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38144639134407043})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39454779028892517})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3999663293361664})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37790992856025696})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47198373079299927})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.391120582818985})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.446698397397995})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9537, 'crossentropy': 0.36769228515625}
store['active_learning_steps'][39]['acquisition']={'indices': [59286, 20150, 42673, 7949, 33391, 33102, 27024, 15757, 28368, 9782], 'labels': [8, 3, 1, -1, 4, 6, 8, 8, 9, 8], 'scores': [0.9626375436782837, 0.9116173386573792, 0.9114462733268738, 0.8889328241348267, 0.8751853704452515, 0.8737547993659973, 0.8701472878456116, 0.8685054183006287, 0.8597365617752075, 0.8574315309524536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.313472032546997})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7147445678710938})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5341370105743408})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43726757168769836})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4101187586784363})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4227684736251831})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4140516519546509})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.421217679977417})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9537, 'crossentropy': 0.371550390625}
store['active_learning_steps'][40]['acquisition']={'indices': [11403, 5679, 31308, 1423, 46284, 49064, 17804, 42136, 3367, 17808], 'labels': [0, 3, 8, 0, 9, 8, 8, 0, 0, 8], 'scores': [0.8790891170501709, 0.8314098119735718, 0.8044629096984863, 0.8003016710281372, 0.7971770763397217, 0.7966504096984863, 0.7943754196166992, 0.7858625054359436, 0.779629111289978, 0.7770723700523376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.40885329246521})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.6231061220169067})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4867762327194214})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4390465021133423})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39812177419662476})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3771517872810364})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36465829610824585})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3109557032585144})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33381593227386475})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34793102741241455})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3784406781196594})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.317800537109375}
store['active_learning_steps'][41]['acquisition']={'indices': [6574, 40732, 19089, 10181, 49518, 44754, 49624, 10260, 42648, 15803], 'labels': [-1, -1, 5, -1, -1, -1, 6, -1, -1, 1], 'scores': [0.994478166103363, 0.9836978316307068, 0.9775631427764893, 0.961733341217041, 0.9556986689567566, 0.9537524580955505, 0.9467309713363647, 0.9327255487442017, 0.932697594165802, 0.9224767684936523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3825980424880981})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7191106081008911})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5152664184570312})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4131671190261841})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4016970992088318})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40872886776924133})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3594498634338379})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35525280237197876})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3913736939430237})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32571089267730713})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3584755063056946})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3897061347961426})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40559443831443787})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.2994849609375}
store['active_learning_steps'][42]['acquisition']={'indices': [23890, 20641, 17739, 18324, 27637, 46975, 38920, 14977, 51236, 21691], 'labels': [-1, 9, 5, 0, -1, -1, 7, -1, -1, -1], 'scores': [0.9164789319038391, 0.9152480959892273, 0.9129142165184021, 0.9085279107093811, 0.9082579612731934, 0.9029073715209961, 0.897400975227356, 0.8892461657524109, 0.8889941573143005, 0.8871296048164368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1635279655456543})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5910838842391968})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38228416442871094})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36439764499664307})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3367171287536621})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32243478298187256})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.328227162361145})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37210363149642944})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.310899019241333})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4016605019569397})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3147081136703491})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35266655683517456})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2846156982421875}
store['active_learning_steps'][43]['acquisition']={'indices': [4955, 45911, 48038, 47936, 52661, 42472, 7949, 18487, 52914, 50946], 'labels': [2, 3, 3, 8, 3, 2, -1, 4, 5, 3], 'scores': [0.9567229151725769, 0.9460801780223846, 0.9390433430671692, 0.9339216947555542, 0.9174543619155884, 0.9168974161148071, 0.9162412881851196, 0.9142693281173706, 0.9116001725196838, 0.9023375511169434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2419840097427368})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6200906038284302})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5366626977920532})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3762344717979431})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3848262429237366})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33878761529922485})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3462671935558319})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34790027141571045})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3532218933105469})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.302187744140625}
store['active_learning_steps'][44]['acquisition']={'indices': [50403, 13779, 32417, 46133, 59187, 17521, 50239, 16755, 15738, 54885], 'labels': [-1, 0, 9, -1, -1, 3, 9, 3, -1, 6], 'scores': [0.8441559672355652, 0.8228952884674072, 0.8151293992996216, 0.8099669218063354, 0.8040538430213928, 0.7995060682296753, 0.7963571548461914, 0.7869266271591187, 0.7862477898597717, 0.7858949899673462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.3433542251586914})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7945976257324219})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5864159464836121})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.46534091234207153})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.401577353477478})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35985487699508667})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3491581082344055})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39328452944755554})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3924127221107483})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3991445302963257})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.326832763671875}
store['active_learning_steps'][45]['acquisition']={'indices': [1075, 1239, 52889, 36256, 56203, 18598, 9384, 36195, 54950, 5443], 'labels': [7, 8, -1, 5, -1, 9, 5, -1, 8, -1], 'scores': [0.9176945686340332, 0.8965488076210022, 0.867730438709259, 0.8348134160041809, 0.8300334215164185, 0.8223088383674622, 0.8209934830665588, 0.8204755783081055, 0.8105339407920837, 0.8092212677001953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.34132981300354})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6953059434890747})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47334572672843933})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39191165566444397})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3598915934562683})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3638715147972107})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34066033363342285})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34466686844825745})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3866516649723053})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35279858112335205})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.3098349853515625}
store['active_learning_steps'][46]['acquisition']={'indices': [27358, 59744, 22320, 16799, 52889, 7308, 11767, 50090, 29320, 15510], 'labels': [8, 6, 8, 9, -1, 8, 4, 4, 1, 2], 'scores': [0.9396596550941467, 0.8989815711975098, 0.8678622245788574, 0.8566769361495972, 0.8551228046417236, 0.8504008650779724, 0.8491831421852112, 0.8454713225364685, 0.8375184535980225, 0.837317168712616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4468013048171997})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.709022045135498})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5066561102867126})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40897437930107117})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36480414867401123})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3519405722618103})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31747278571128845})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33530107140541077})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3401273488998413})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31623098254203796})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34093743562698364})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32465028762817383})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3040130138397217})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3245050013065338})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3370678424835205})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3570139408111572})
store['active_learning_steps'][47]['training']['best_epoch']=13
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.284455322265625}
store['active_learning_steps'][47]['acquisition']={'indices': [52889, 47626, 43524, 49282, 52834, 7949, 8883, 43112, 5298, 12168], 'labels': [-1, -1, -1, 2, 2, -1, 2, -1, 0, -1], 'scores': [1.053208351135254, 1.0201401710510254, 0.9768723845481873, 0.9581184983253479, 0.9556105136871338, 0.9533265233039856, 0.9495358467102051, 0.9473556876182556, 0.9436860084533691, 0.9414147734642029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3705276250839233})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6688336133956909})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4886792302131653})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3927130103111267})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3543948531150818})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.373782753944397})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36043184995651245})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36096304655075073})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.3520336181640625}
store['active_learning_steps'][48]['acquisition']={'indices': [19942, 5052, 8849, 53990, 59747, 26721, 40654, 13524, 12650, 24141], 'labels': [5, 0, 7, -1, 5, 7, 5, 3, 5, 7], 'scores': [0.8043559789657593, 0.7816132307052612, 0.7782037258148193, 0.7711579203605652, 0.7586408257484436, 0.7481368780136108, 0.7477438449859619, 0.7450289130210876, 0.7337836623191833, 0.730211615562439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3784793615341187})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7695205211639404})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5193412899971008})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4180781841278076})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37530621886253357})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36448073387145996})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3621330261230469})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3313150405883789})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4123150706291199})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3555717468261719})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3428339958190918})
store['active_learning_steps'][49]['training']['best_epoch']=8
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.291096435546875}
